from pydantic import BaseModel, Field

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
    description='Dialysis at least twice in the past seven days or 24-hours of continuous hemodialysis within the '
                'prior 7 days.'
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
var_description['sodium'] = Field(
    default=137.0,
    title='Serum sodium',
    description='Also known as \'Na.\' This is the patient\'s serum sodium in mg/dL and should be in a range between '
                '110 and 160',
    gt=110,
    lt=160
)


# caprini ------------------------------------------------------

var_description['age'] = Field(
    default=55,
    title="Age",
    description="Age in years",
    gt=18,
    lt=120
)
var_description['sex'] = Field(
    default="F",
    title="Sex",
    description="Recognized sex of the patient, M or F"
)
var_description['type_of_surgery'] = Field(
    default="not scheduled for surgery",
    title="Type of surgery",
    description="Minor surgery does not refer to type of surgery but rather length of anesthesia <45 minutes. Major "
                "surgery refers to procedures with general or regional anesthesia time exceeding 45 minutes. Major"
                "lower extremity surgery refers to procedures anesthesia time exceeding 45 minutes and involving "
                "the hip, knee, thigh, or ankle."
)
var_description['recent_major_surgery'] = Field(
    default=False,
    title="Recent major surgery",
    description="In last 30 days, has patient had major surgery, defined as anesthesia time >45 minutes?",
    points=1
)
var_description['recent_chf'] = Field(
    default=False,
    title="Recent congestive heart failure",
    description="In last 30 days, has patient had heart failure?",
    points=1
)
var_description['recent_sepsis'] = Field(
    default=False,
    title="Recent sepsis",
    description="In last 30 days, has patient had sepsis, been hospitalized for an infection, or required IV "
                "antibiotics. Do not count pneumonia under this category?",
    points=1
)
var_description['recent_pna'] = Field(
    default=False,
    title="Recent pneumonia",
    description="In last 30 days, has patient had pneumonia or recieved IV antibiotics for a lung infection?",
    points=1
)
var_description['recent_preg'] = Field(
    default=False,
    title="Recent pregnancy or postpartum",
    description="In last 30 days, has patient been pregnant or postpartum?",
    points=1
)

var_description['recent_cast'] = Field(
    default=False,
    title="Recent immobilizing plaster cast",
    description="In last 30 days, has patient had an immobilizing plaster cast?",
    points=2
)
var_description['recent_fracture'] = Field(
    default=False,
    title="Recent hip, pelvis, or leg fracture",
    description="In last 30 days, has patient had a hip, pelvis, or leg fracture?",
    points=5
)
var_description['recent_stroke'] = Field(
    default=False,
    title="Recent stroke",
    description="In last 30 days, has patient had stroke?",
    points=5
)
var_description['recent_trauma'] = Field(
    default=False,
    title="Recent multiple trauma",
    description="In last 30 days, has patient had multiple trauma?",
    points=5
)
var_description['recent_spinal_cord_injury'] = Field(
    default=False,
    title="Recent acute spinal cord injury causing paralysis",
    description="In last 30 days, has patient had a acute spinal cord injury causing paralysis?",
    points=5
)
var_description['varicose_veins'] = Field(
    default=False,
    title="Varicose veins",
    description="Does the patient have varicose veins?",
    points=1
)
var_description['current_swollen_legs'] = Field(
    default=False,
    title="Current swollen legs",
    description="Does the patient have a current swollen legs?",
    points=1
)
var_description['current_central_venous_access'] = Field(
    default=False,
    title="Current central venous access",
    description="Does the patient have a current central venous access?",
    points=2
)
var_description['history_of_dvt_pe'] = Field(
    default=False,
    title="History of DVT/PE",
    description="Does the patient have a history of DVT/PE?",
    points=3
)
var_description['family_history_of_thrombosis'] = Field(
    default=False,
    title="Family history of thrombosis",
    description="Does the patient have a family history of thrombosis?",
    points=3
)
var_description['positive_factor_v_leiden'] = Field(
    default=False,
    title="Positive Factor V Leiden",
    description="Does the patient have a positive Factor V Leiden?",
    points=3
)
var_description['positive_prothrombin_20210a'] = Field(
    default=False,
    title="Positive prothrombin 20210A",
    description="Does the patient have a positive prothrombin 20210A?",
    points=3
)
var_description['elevated_serum_homocysteine'] = Field(
    default=False,
    title="Elevated serum homocysteine",
    description="Does the patient have a elevated serum homocysteine?",
    points=3
)
var_description['positive_lupus_anticoagulant'] = Field(
    default=False,
    title="Positive lupus anticoagulant",
    description="Does the patient have a positive lupus anticoagulant?",
    points=3
)
var_description['elevated_anticardiolipin_antibody'] = Field(
    default=False,
    title="Elevated anticardiolipin antibody",
    description="Does the patient have a elevated anticardiolipin antibody?",
    points=3
)
var_description['heparin_induced_thrombocytopenia'] = Field(
    default=False,
    title="Heparin-induced thrombocytopenia",
    description="Does the patient have heparin-induced thrombocytopenia?",
    points=3
)
var_description['other_congenital_or_acquired_thrombophilia'] = Field(
    default=False,
    title="Other congenital or acquired thrombophilia",
    description="Does the patient have any other congenital or acquired thrombophilia?",
    points=3
)
var_description['mobility'] = Field(
    default='normal/ambulatory',
    title="Mobility",
    description="There are three categories of mobility: normal/ambulatory, bedrest/only walking in room;"
                " or confined to bed >72 hours."
)
var_description['history_of_inflammatory_bowel_disease'] = Field(
    default=False,
    title="History of inflammatory bowel disease",
    description="Does the patient have a history of inflammatory bowel disease?",
    points=1
)
var_description['bmi'] = Field(
    default=22,
    title="BMI",
    description="Body mass index (BMI) of patient in kg/m2?"
)
var_description['acute_mi'] = Field(
    default=False,
    title="Acute MI",
    description="Does the patient have an acute MI?",
    points=1
)
var_description['copd'] = Field(
    default=False,
    title="COPD",
    description="Does the patient have COPD?",
    points=1
)
var_description['present_or_previous_malignancy'] = Field(
    default=False,
    title="Present or previous malignancy",
    description="Does the patient have a present or previous malignancy?",
    points=1
)
var_description['other_risk_factors'] = Field(
    default=False,
    title="Other risk factors",
    description="Does the patient have any other risk factors for VTE?",
    points=1
)


# wells dvt ------------------------------------------------------

var_description['active_cancer'] = Field(
    default=False,
    title="Active cancer",
    description="Does the patient have active cancer (treatment or palliation within 6 months)?"
)
var_description['bedridden_recently'] = Field(
    default=False,
    title="Bedridden recently",
    description="Has the patient been bedridden recently (greater than 3 days) or had major surgery within 12 weeks?"
)
var_description['calf_swelling'] = Field(
    default=False,
    title="Calf swelling",
    description="Does the patient have calf swelling greater than 3 cm compared to the other leg? (measured 10 cm below tibial tuberosity)"
)
var_description['collateral_veins'] = Field(
    default=False,
    title="Collateral veins",
    description="Does the patient have collateral (nonvaricose) superficial veins?"
)
var_description['entire_leg_swollen'] = Field(
    default=False,
    title="Entire leg swollen",
    description="Does that patient have an entire leg which is swollen?"
)
var_description['localized_tenderness'] = Field(
    default=False,
    title="Localized tenderness",
    description="Does the patient have localized tenderness along a deep venous system?"
)
var_description['pitting_edema'] = Field(
    default=False,
    title="Pitting edema",
    description="Does the patient have pitting edema, confined to symptomatic leg?"
)
var_description['paralysis_paresis_or_plaster'] = Field(
    default=False,
    title="Paralysis, paresis, or plaster immobilization",
    description="Does the patient have paralysis, paresis, or recent plaster immobilization of the lower extremity?"
)
var_description['previous_dvt'] = Field(
    default=False,
    title="Previously documented DVT",
    description="Does the patient have previously-documented DVT?"
)
var_description['alternative_diagnosis_as_likely'] = Field(
    default=False,
    title="Alternative diagnosis to DVT",
    description="Does the patient have alternative diagnosis to DVT as likely or more likely?"
)


if __name__ == "__main__":
    print("you've reached this message in error")
