# Project:     open-med-calc
# File:        api/main.py
# Created by:  Alex Goodell
import os

# ============== Imports ==============

from fastapi import FastAPI, Request

from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field
import numpy as np
from variable_descriptions import *
from model_classes import *
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import markdown

# ============== Functions ==============

def calc_docs(calculator_name: str):
    return Path(f'calculator_docs/short_calculator_info/{calculator_name}.md').read_text()

def full_calculator_pages(calculator_name: str):
    md_text = Path(f'calculator_docs/full_calculator_pages/{calculator_name}.md').read_text()
    return md_text

# ============== Content server ==============

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/contact", response_class=HTMLResponse)
async def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

# -------------------------------------------- redirects --------------------------------------------

redirects = [
    {'from': '/meld',      'to': '/meld-na'},
    {'from': '/chatbot',   'to': 'https://chat.openai.com/g/g-mtNkUsX41-openmedcalc'},
    {'from': '/bot',       'to': 'https://chat.openai.com/g/g-mtNkUsX41-openmedcalc'},
    {'from': '/chat',      'to': 'https://chat.openai.com/g/g-mtNkUsX41-openmedcalc'},
    {'from': '/paper',      'to': 'https://www.medrxiv.org/content/10.1101/2023.12.13.23299881v1'},
    {'from': '/preprint',      'to': 'https://www.medrxiv.org/content/10.1101/2023.12.13.23299881v1'}
]

for redirect in redirects:
    app.get(redirect['from'], lambda: RedirectResponse(url=redirect['to']))


# ------------------------------------ about calculator pages -------------------------------------

async def read_full_calculator_page(request: Request):
    # get route
    route_last = str(request.url).split("/")[-1]
    content = markdown.markdown(full_calculator_pages(route_last))
    return templates.TemplateResponse("blank.html", {"request": request, "content": content})

# for each file in calculator_docs/full_calculator_pages, add a route
for file in Path('calculator_docs/full_calculator_pages').glob('*.md'):
    app.add_route(f'/{file.stem}', read_full_calculator_page)

# ============== API ==============

if os.environ.get('IS_LOCAL_ENV'):
    openapi_url = "/api/openapi.json"
    api_root = "http://localhost:7777/api"
else:
    openapi_url = "https://api.openmedcalc.org/openapi.json"
    api_root = "https://api.openmedcalc.org/"


api = FastAPI(
    swagger_ui_parameters={"url": openapi_url,
                           "openapi_url": openapi_url},
    title="OpenMedCalc API",
    description="OpenMedCalc API helps you calculate medical scores and indices.",
    summary="The open source medical calculator",
    terms_of_service="http://openmedcalc.org/about",
    contact={
        "name": "OpenMedCalc",
        "url": "http://openmedcalc.org/contact",
        "email": "info@openmedcalc.org",
    },
    servers=[{'url': api_root, 'description': 'primary SSL endpoint'}],
    root_path="/api",
    root_path_in_servers=False
)
app.mount("/api", api)


# 404
@app.api_route("/{path_name:path}", methods=["GET"], response_class=HTMLResponse)
async def catch_all(request: Request, path_name: str):
    return templates.TemplateResponse("index.html", {"request": request})


# ================= API Routes ==================


# ----------------- Welcome -----------------
@api.get("/", summary="Welcome")
async def welcome():
    return {"message": 'Welcome to the open-med-calc API. Please see the documentation at /docs for more information'}


# ------------- Original MELD -----------------

@api.post("/meld", summary="Calculate Original MELD Score", response_model=CalcResponse, description=calc_docs('meld'))
async def calculate_meld(calc: CalcRequestMeld):
    additional_info = calc_docs('meld')
    # (0.957 * ln(Serum Cr) + 0.378 * ln(Serum Bilirubin) + 1.120 * ln(INR) + 0.643 ) * 10
    if calc.is_on_dialysis:
        calc.creatinine = 4.0
    meld_score = (0.957 * np.log(calc.creatinine) + 0.378 * np.log(
        calc.bilirubin) + 1.120 * np.log(calc.inr) + 0.643) * 10
    meld_score = int(np.round(meld_score, 0))
    # Estimated 3-Month Mortality By MELD Score
    # ≤9 1.9%
    # 10–19 6.0%
    # 20–29 19.6%
    # 30–39 52.6%
    # ≥40 71.3%

    three_month_mortality = 0
    if meld_score <= 9:
        three_month_mortality = 1.9
    elif meld_score <= 19:
        three_month_mortality = 6.0
    elif meld_score <= 29:
        three_month_mortality = 19.6
    elif meld_score <= 39:
        three_month_mortality = 52.6
    else:
        three_month_mortality = 71.3
    message = "The patient's MELD score is " + str(meld_score) + ". The estimated 3-month mortality is " + str(
        three_month_mortality) + "%."
    response = CalcResponse(success=True, score=meld_score, message=message, additional_info=additional_info)
    return response


# -------------- MELD-Na -----------------

@api.post("/meld-na", summary="Calculate MELD-Na Score", response_model=CalcResponse, description=calc_docs('meld-na'))
async def calculate_meld_na(calc: CalcRequestMeldNa):
    additional_info = calc_docs('meld-na')

    # All values in US units (Cr and bilirubin in mg/dL, Na in mEq/L, and INR unitless).
    # If bilirubin, Cr, or INR is <1.0, use 1.0.
    if calc.creatinine < 1:
        calc.creatinine = 1
    if calc.bilirubin < 1:
        calc.bilirubin = 1
    if calc.inr < 1:
        calc.inr = 1

    # If any of the following is true, use Cr 4.0:
    # Cr >4.0.
    # ≥2 dialysis treatments within the prior 7 days.
    # 24 hours of continuous veno-venous hemodialysis (CVVHD) within the prior 7 days.
    if calc.creatinine > 4:
        calc.creatinine = 4
    if calc.is_on_dialysis == 1:
        calc.creatinine = 4

    # If Na <125 mmol/L, use 125. If Na >137 mmol/L, use 137.
    if calc.sodium < 125:
        calc.sodium = 125
    if calc.sodium > 137:
        calc.sodium = 137

    # first calculate the MELD(i) = 0.957 × ln(Cr) + 0.378 × ln(bilirubin) + 1.120 × ln(INR) + 0.643
    # Then, round to the tenth decimal place and multiply by 10.
    # confirmed:  np.log is natural log
    meld_i = 0.957 * np.log(calc.creatinine) + 0.378 * np.log(calc.bilirubin) + 1.12 * np.log(calc.inr) + 0.643
    meld_i = np.round(meld_i, 2) * 10.0

    # If MELD(i) > 11, perform additional MELD calculation as follows:
    # MELD = MELD(i) + 1.32 × (137 – Na) –  [ 0.033 × MELD(i) × (137 – Na) ]
    if meld_i > 11:
        meld_na = meld_i + 1.32 * (137 - calc.sodium) - (0.033 * meld_i * (137 - calc.sodium))
    else:
        meld_na = meld_i

    # cannot be higher than 40
    if meld_na > 40:
        meld_na = 40

    # round to nearest integer
    meld_na = np.round(meld_na, 0)

    three_month_mortality = 0
    if meld_na <= 9:
        three_month_mortality = 1.9
    elif meld_na <= 19:
        three_month_mortality = 6.0
    elif meld_na <= 29:
        three_month_mortality = 19.6
    elif meld_na <= 39:
        three_month_mortality = 52.6
    else:
        three_month_mortality = 71.3
    message = "The patient's MELD-Na score is " + str(meld_na) + ". The estimated 3-month mortality is " + str(
        three_month_mortality) + "%."
    response = CalcResponse(success=True, score=meld_na, message=message, additional_info=additional_info)
    return response


# -------------- Caprini VTE -----------------

@api.post("/caprini-vte", summary="Calculate the Caprini Score for Venous Thromboembolism", response_model=CalcResponse,
          description=calc_docs('caprini-vte'))
async def calculate_caprini(calc: CalcRequestCapriniVte):
    additional_info = calc_docs('caprini-vte')

    caprini_vte_score = 0

    # age
    if calc.age < 41:
        caprini_vte_score += 0
    if calc.age >= 41 and calc.age <= 60:
        caprini_vte_score += 1
    if calc.age >= 61 and calc.age <= 74:
        caprini_vte_score += 2
    if calc.age >= 75:
        caprini_vte_score += 3

    # sex has no impact on score
    if calc.sex == calc.sex.male:
        caprini_vte_score += 0
    elif calc.sex == calc.sex.male:
        caprini_vte_score += 0

    # type of surgery
    if calc.type_of_surgery == calc.type_of_surgery.none:
        caprini_vte_score += 0
    elif calc.type_of_surgery == calc.type_of_surgery.minor:
        caprini_vte_score += 1
    elif calc.type_of_surgery == calc.type_of_surgery.major:
        caprini_vte_score += 2
    elif calc.type_of_surgery == calc.type_of_surgery.major_lower_extremity:
        caprini_vte_score += 5

    # mobility
    if calc.mobility == calc.mobility.ambulatory:
        caprini_vte_score += 0
    elif calc.mobility == calc.mobility.bedrest:
        caprini_vte_score += 1
    elif calc.mobility == calc.mobility.confined:
        caprini_vte_score += 2

    # BMI
    if calc.bmi <= 25:
        caprini_vte_score += 0
    elif calc.bmi > 25:
        caprini_vte_score += 1

    if calc.recent_major_surgery:
        caprini_vte_score += 1
    if calc.recent_chf:
        caprini_vte_score += 1
    if calc.recent_sepsis:
        caprini_vte_score += 1
    if calc.recent_pna:
        caprini_vte_score += 1
    if calc.recent_preg:
        caprini_vte_score += 1

    if calc.recent_cast:
        caprini_vte_score += 2

    if calc.recent_fracture:
        caprini_vte_score += 5
    if calc.recent_stroke:
        caprini_vte_score += 5
    if calc.recent_trauma:
        caprini_vte_score += 5
    if calc.recent_spinal_cord_injury:
        caprini_vte_score += 5

    if calc.varicose_veins:
        caprini_vte_score += 1
    if calc.current_swollen_legs:
        caprini_vte_score += 1

    if calc.current_central_venous_access:
        caprini_vte_score += 2

    if calc.history_of_dvt_pe:
        caprini_vte_score += 3
    if calc.family_history_of_thrombosis:
        caprini_vte_score += 3
    if calc.positive_factor_v_leiden:
        caprini_vte_score += 3
    if calc.positive_prothrombin_20210a:
        caprini_vte_score += 3
    if calc.elevated_serum_homocysteine:
        caprini_vte_score += 3
    if calc.positive_lupus_anticoagulant:
        caprini_vte_score += 3
    if calc.elevated_anticardiolipin_antibody:
        caprini_vte_score += 3
    if calc.heparin_induced_thrombocytopenia:
        caprini_vte_score += 3
    if calc.other_congenital_or_acquired_thrombophilia:
        caprini_vte_score += 3

    if calc.history_of_inflammatory_bowel_disease:
        caprini_vte_score += 1
    if calc.acute_mi:
        caprini_vte_score += 1
    if calc.copd:
        caprini_vte_score += 1
    if calc.present_or_previous_malignancy:
        caprini_vte_score += 2
    if calc.other_risk_factors:
        caprini_vte_score += 1

    # risk category
    if caprini_vte_score == 0:
        risk_category = "Lowest"
        risk_percent = "minimal"
    elif 1 <= caprini_vte_score <= 2:
        risk_category = "low"
        risk_percent = "minimal"
    elif 3 <= caprini_vte_score <= 4:
        risk_category = "moderate"
        risk_percent = "0.7%"
    elif 5 <= caprini_vte_score <= 6:
        risk_category = "high"
        risk_percent = "1.8%"
    elif 7 <= caprini_vte_score <= 8:
        risk_category = "high"
        risk_percent = "4.0%"
    elif caprini_vte_score >= 9:
        risk_category = "highest"
        risk_percent = "10.7%"

    #
    # | Caprini Score | Risk category | Risk percent* | Recommended prophylaxis** | Duration of chemoprophylaxis |
    # | 0 | Lowest | Minimal | Early frequent ambulation only, OR at discretion of surgical team: Pneumatic compression devices OR graduated compression stockings | During hospitalization |
    # | 1–2 | Low | Minimal | Pneumatic compression devices ± graduated compression stockings | During hospitalization |
    # | 3–4 | Moderate | 0.7% | Pneumatic compression devices ± graduated compression stockings | During hospitalization |
    # | 5–6 | High | 1.8% | Pneumatic compression devices AND low dose heparin OR low molecular weight heparin | 7–10 days total |
    # | 7-8 | High | 4.0% | Pneumatic compression devices AND low dose heparin OR low molecular weight heparin | 7–10 days total |
    # | ≥9 | Highest | 10.7% | Pneumatic compression devices AND low dose heparin OR low molecular weight heparin | 30 days total |

    message = f"The patient's Caprini VTE risk score is {caprini_vte_score}. This correlates to a {risk_category} risk category and a {risk_percent} risk of VTE during a hospital admission."
    response = CalcResponse(success=True, score=caprini_vte_score, message=message, additional_info=additional_info)
    return response


# -------------- Wells DVT -----------------

@api.post("/wells-dvt", summary="Calculate Wells Criteria for DVT", response_model=CalcResponse,
          description=calc_docs('wells-dvt'))
async def calculate_wells_dvt(calc: CalcRequestWellsDvt):
    additional_info = calc_docs('wells-dvt')

    wells_dvt_score = 0
    if calc.active_cancer:
        wells_dvt_score += 1
    if calc.bedridden_recently:
        wells_dvt_score += 1
    if calc.calf_swelling:
        wells_dvt_score += 1
    if calc.collateral_veins:
        wells_dvt_score += 1
    if calc.entire_leg_swollen:
        wells_dvt_score += 1
    if calc.localized_tenderness:
        wells_dvt_score += 1
    if calc.pitting_edema:
        wells_dvt_score += 1
    if calc.paralysis_paresis_or_plaster:
        wells_dvt_score += 1
    if calc.previous_dvt:
        wells_dvt_score += 1
    if calc.alternative_diagnosis_as_likely:
        wells_dvt_score += -2

    if wells_dvt_score == 0:
        risk_category = "low/unlikely"
        prevalence_of_dvt = "5%"
    if wells_dvt_score == 1 or wells_dvt_score == 2:
        risk_category = "moderate"
        prevalence_of_dvt = "17%"
    if wells_dvt_score >= 3:
        risk_category = "high/likely"
        prevalence_of_dvt = "17-53%"

    message = (f"The patient's Wells Criteria for DVT score is {wells_dvt_score}. This corresponds to a {risk_category}"
               f" risk category; individuals in this group had a {prevalence_of_dvt} prevalence of deep vein thrombosis.")
    response = CalcResponse(success=True, score=wells_dvt_score, message=message, additional_info=additional_info)
    return response


# -------------- PSI/PORT -----------------
@api.post("/psi-port", summary="Calculate the PSI/PORT Score Pneumonia Severity Index for CAP",
          response_model=CalcResponse,
          description=calc_docs('psi-port'))
async def calculate_psi_port(calc: CalcRequestPsiPort):
    additional_info = calc_docs('psi-port')

    psi_port_score = 0

    # demographic: age & gender
    psi_port_score += calc.age
    if calc.sex != calc.sex.male:
        psi_port_score -= 10
    elif calc.sex == calc.sex.male:
        psi_port_score += 0

    # nursing home resident
    if calc.nursing_home_resident:
        psi_port_score += 10

    # Coexisting illnesses
    if calc.neoplastic_disease:
        psi_port_score += 30
    if calc.liver_disease:
        psi_port_score += 20
    if calc.congestive_heart_failure:
        psi_port_score += 10
    if calc.cerebrovascular_disease:
        psi_port_score += 10
    if calc.renal_disease:
        psi_port_score += 10

    # physical examination
    if calc.altered_mental_status:
        psi_port_score += 20
    if calc.respiratory_rate >= 30:
        psi_port_score += 20
    if calc.systolic_bp < 90:
        psi_port_score += 20
    if calc.pulse >= 125:
        psi_port_score += 10
    if calc.temperature < 35 or calc.temperature > 40:
        psi_port_score += 15
    # lab and radiographic findings
    if calc.ph < 7.35:
        psi_port_score += 30
    if calc.bun >= 30:
        psi_port_score += 20
    if calc.sodium_mmol_L < 130:
        psi_port_score += 20
    # glucose mg/dL
    if calc.glucose >= 250:
        psi_port_score += 10
    # glucose mmol/L
    elif calc.glucose >= 14:
        psi_port_score += 10
    if calc.hematocrit < 30:
        psi_port_score += 10
    if calc.pao2 < 60:
        psi_port_score += 10
    if calc.pleural_effusion:
        psi_port_score += 10

    # risk category
    if psi_port_score <= 50:
        risk_category = "low"
        risk_class = "I"
    elif 50 <= psi_port_score <= 70:
        risk_category = "low"
        risk_class = "II"
    elif 71 <= psi_port_score <= 90:
        risk_category = "moderate"
        risk_class = "III"
    elif 91 <= psi_port_score <= 130:
        risk_category = "high"
        risk_class = "IV"
    elif psi_port_score >= 130:
        risk_category = "high"
        risk_class = "V"
    if psi_port_score < 50 & calc.age >= 50:
        risk_category = "low"
        risk_class = "II"

    # | PSI/PORT Score | Risk class | Risk category | Recommended disposition |
    # | <=50 | I | Low risk | Outpatient care |
    # | <= 70 | II | Low risk | Outpatient care |
    # | 71-90 | III | Low risk | Outpatient vs. Observation admission |
    # | 91-130 | IV | Medium risk | Inpatient admission |
    # | >=130 | V | High risk | Inpatient admission |

    message = f"The patient's PSI/PORT score is {psi_port_score}. This correlates to a risk class {risk_class} with {risk_category} risk mortality for patients with community-acquired pneumonia."
    response = CalcResponse(success=True, score=psi_port_score, message=message, additional_info=additional_info)
    return response
