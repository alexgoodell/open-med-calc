# Project:     open-med-calc
# File:        app/main.py
# Created by:  Alex Goodell

# ============== Imports ==============

from fastapi import FastAPI
from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field
import numpy as np

# ============== Description ==============

description = """
OpenMedCalc API helps you calculate medical scores and indices.
"""

app = FastAPI(
    title="OpenMedCalc API",
    description=description,
    summary="The open source medical calculator",
    version="0.0.1",
    terms_of_service="http://openmedcalc.org/terms/",
    contact={
        "name": "OpenMedCalc",
        "url": "http://openmedcalc.org/contact/",
        "email": "info@openmedcalc.org",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# ============== Variable descriptions ==============

var_description = dict()

var_description['success'] = Field(
    default=False,
    title='Success',
    description='Describes whether the calculation was successful or not.'
)
var_description['message'] = Field(
    default="message",
    title='Result message',
    description='Summarizes the results of the caluclation'
)
var_description['additional_info'] = Field(
    default="info",
    title='Result information',
    description='Summarizes important information about the calculation'
)

var_description['inr'] = Field(
    default=1.0,
    title='International Normalized Ratio',
    description='This is the patient\'s INR value and should be between 0 and 10',
    gt=0,
    lt=10
)
var_description['is_on_dialysis'] = Field(
    default=False,
    title='Is the patient on dialysis?',
    description='Dialysis at least twice in the past week'
)
var_description['bilirubin'] = Field(
    default=1.0,
    title='Serum bilirubin',
    description='This is the patient\'s total bilirubin value in mg/dL and should be between 0 and 10',
    gt=0,
    lt=10
)
var_description['creatinine'] = Field(
    default=1.0,
    title='Serum creatinine',
    description='This is the patient\'s serum creatinine in mg/dL and should be between 0 and 10',
    gt=0,
    lt=10
)


class CalcRequestMeld(BaseModel):
    is_on_dialysis: bool = var_description['is_on_dialysis']
    creatinine: float = var_description['creatinine']
    bilirubin: float = var_description['bilirubin']
    inr: float = var_description['inr']


class CalcResponse(BaseModel):
    success: bool = var_description['success']
    score: Optional[int]
    message: Optional[str] = var_description['message']
    additional_info: Optional[str] = var_description['additional_info']


@app.get("/api/calc/")
def welcome():
    return {"message": 'Welcome to the open-med-calc API. Please see the documentation at /docs for more information'}


@app.post("/api/calc/meld", description=Path('docs/meld.md').read_text(), summary="Calculate Original MELD Score", response_model=CalcResponse)
def calculate_meld(calcRequestMeld: CalcRequestMeld):
    additional_info = ('See openmedcalc.org/meld for references. Note this version has been suppplanted by the MELD-Na '
                       'score and the MELD 3.0 score.')
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
