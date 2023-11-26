# Project:     open-med-calc
# File:        app/main.py
# Created by:  Alex Goodell

# ============== Imports ==============

from fastapi import FastAPI

from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field
import numpy as np
from variable_descriptions import var_description

# ============== Description ==============

app = FastAPI(
    title="OpenMedCalc API",
    description="OpenMedCalc API helps you calculate medical scores and indices.",
    summary="The open source medical calculator",
    terms_of_service="http://openmedcalc.org/terms/",
    contact={
        "name": "OpenMedCalc",
        "url": "http://openmedcalc.org/contact/",
        "email": "info@openmedcalc.org",
    },
    servers=[{'url': 'https://api.openmedcalc.org', 'description': 'primary SSL endpoint'}]
)


def calc_docs(calculator_name: str):
    return Path('calculator_docs/meld.md').read_text()


# ============== Models ==============

# basic response model
class CalcResponse(BaseModel):
    success: bool = var_description['success']
    score: Optional[int]
    message: Optional[str] = var_description['message']
    additional_info: Optional[str] = var_description['additional_info']

# original meld
class CalcRequestMeld(BaseModel):
    is_on_dialysis: bool = var_description['is_on_dialysis']
    creatinine: float = var_description['creatinine']
    bilirubin: float = var_description['bilirubin']
    inr: float = var_description['inr']


# meld sodium
class CalcRequestMeldNa(BaseModel):
    is_on_dialysis: bool = var_description['is_on_dialysis']
    creatinine: float = var_description['creatinine']
    bilirubin: float = var_description['bilirubin']
    inr: float = var_description['inr']
    sodium: float = var_description['sodium']



@app.get("/", summary="Welcome")
def welcome():
    return {"message": 'Welcome to the open-med-calc API. Please see the documentation at /docs for more information'}


@app.post("/meld", summary="Calculate Original MELD Score", response_model=CalcResponse, description=calc_docs('meld'))
def calculate_meld(calcRequestMeld: CalcRequestMeld):
    additional_info = calc_docs('meld')
    # (0.957 * ln(Serum Cr) + 0.378 * ln(Serum Bilirubin) + 1.120 * ln(INR) + 0.643 ) * 10
    if calcRequestMeld.is_on_dialysis:
        calcRequestMeld.creatinine = 4.0
    meld_score = (0.957 * np.log(calcRequestMeld.creatinine) + 0.378 * np.log(
        calcRequestMeld.bilirubin) + 1.120 * np.log(calcRequestMeld.inr) + 0.643) * 10
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

