from pydantic import BaseModel
from variable_descriptions import var_description
from typing import Optional
from enum import Enum


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


# -------------  caprini vte -----------------
class SurgeryType(Enum):
    none = "not scheduled for surgery"
    minor = "minor surgery"
    major = "major surgery"
    major_lower_extremity = "major lower extremity surgery"

class Mobility(Enum):
    ambulatory = "normal/ambulatory"
    bedrest = "bedrest or only walking in room"
    confined = "confined to bed >72 hours"

class Sex(Enum):
    male = "M"
    female = "F"

class CalcRequestCapriniVte(BaseModel):
    age: int = var_description['age']
    sex: Sex = var_description['sex']
    type_of_surgery: SurgeryType = var_description['type_of_surgery']
    recent_major_surgery: bool = var_description['recent_major_surgery']
    recent_chf: bool = var_description['recent_chf']
    recent_sepsis: bool = var_description['recent_sepsis']
    recent_pna: bool = var_description['recent_pna']
    recent_preg: bool = var_description['recent_preg']
    recent_cast: bool = var_description['recent_cast']
    recent_fracture: bool = var_description['recent_fracture']
    recent_stroke: bool = var_description['recent_stroke']
    recent_trauma: bool = var_description['recent_trauma']
    recent_spinal_cord_injury: bool = var_description['recent_spinal_cord_injury']
    varicose_veins: bool = var_description['varicose_veins']
    current_swollen_legs: bool = var_description['current_swollen_legs']
    current_central_venous_access: bool = var_description['current_central_venous_access']
    history_of_dvt_pe: bool = var_description['history_of_dvt_pe']
    family_history_of_thrombosis: bool = var_description['family_history_of_thrombosis']
    positive_factor_v_leiden: bool = var_description['positive_factor_v_leiden']
    positive_prothrombin_20210a: bool = var_description['positive_prothrombin_20210a']
    elevated_serum_homocysteine: bool = var_description['elevated_serum_homocysteine']
    positive_lupus_anticoagulant: bool = var_description['positive_lupus_anticoagulant']
    elevated_anticardiolipin_antibody: bool = var_description['elevated_anticardiolipin_antibody']
    heparin_induced_thrombocytopenia: bool = var_description['heparin_induced_thrombocytopenia']
    other_congenital_or_acquired_thrombophilia: bool = var_description['other_congenital_or_acquired_thrombophilia']
    mobility: Mobility = var_description['mobility']
    history_of_inflammatory_bowel_disease: bool = var_description['history_of_inflammatory_bowel_disease']
    bmi: int = var_description['bmi']
    acute_mi: bool = var_description['acute_mi']
    copd: bool = var_description['copd']
    present_or_previous_malignancy: bool = var_description['present_or_previous_malignancy']
    other_risk_factors: bool = var_description['other_risk_factors']

# -------------  wells DVT -----------------
class CalcRequestWellsDvt(BaseModel):
    active_cancer: bool = var_description['active_cancer']
    bedridden_recently: bool = var_description['bedridden_recently']
    calf_swelling: bool = var_description['calf_swelling']
    collateral_veins: bool = var_description['collateral_veins']
    entire_leg_swollen: bool = var_description['entire_leg_swollen']
    localized_tenderness: bool = var_description['localized_tenderness']
    pitting_edema: bool = var_description['pitting_edema']
    paralysis_paresis_or_plaster: bool = var_description['paralysis_paresis_or_plaster']
    previous_dvt: bool = var_description['previous_dvt']
    alternative_diagnosis_as_likely: bool = var_description['alternative_diagnosis_as_likely']

if __name__ == "__main__":
    print("you've reached this message in error")
