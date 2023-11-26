

  def get_meldna_score(self):
        
        
        

Age 
Sex
Type of surgery
















Varicose veins
Current swollen legs
Current central venous access
History of DVT/PE
Family history of thrombosis
Positive Factor V Leiden
Positive prothrombin 20210A
Elevated serum homocysteine
Positive lupus anticoagulant
Elevated anticardiolipin antibody
Heparin-induced thrombocytopenia
Other congenital or acquired thrombophilia
Mobility
History of inflammatory bowel disease
BMI >25
Acute MI
COPD
Present or previous malignancy
Other risk factors






age_cat = [{ "text" : "≤40", "score": 0},
{ "text" : "41-60", "score": 1},
{ "text" : "61-74", "score": 2},
{ "text" : "≥75", "score": 3}] 

sex_cat = [{ "text" : "man", "score": 0},
{ "text" : "woman", "score": 0}]
recent_history_cat = [{ "text" : "Major surgery", "score": 1},
{ "text" : "a CHF exacerbation", "score": 1},
{ "text" : "an admission for sepsis", "score": 1},
{ "text" : "an admission for pneumonia", "score": 1},
# { "text"" : "Pregnancy or postpartum", "score": 1}, excluded to reduce likelihood of gender confusion being a distraction
{ "text" : "a radial fracture requiring an immobilizing plaster cast", "score": 2},
{ "text" : "a pelvic fracture", "score": 5},
{ "text" : "stroke with minimal residual deficits", "score": 5},
{ "text" : "multiple traumatic falls", "score": 5},
{ "text" : "acute spinal cord injury causing paralysis", "score": 5}]
venous_disease_cat = [{ "text" : "varicose veins", "score": 1},
{ "text" : "current swollen legs", "score": 1},
{ "text" : "current central venous access", "score": 2},
{ "text" : "history of DVT/PE", "score": 3},
# { "text" : "family history of thrombosis", "score": 3}, excluded given family history is hard to code
{ "text" : "positive Factor V Leiden", "score": 3},
{ "text" : "positive prothrombin 20210A", "score": 3},
{ "text" : "elevated serum homocysteine", "score": 3},
{ "text" : "positive lupus anticoagulant", "score": 3},
{ "text" : "elevated anticardiolipin antibody", "score": 3},
{ "text" : "heparin-induced thrombocytopenia", "score": 3}]
# { "text" : "other congenital or acquired thrombophilia", "score": 3}] excluded given confusing wording
mobility_cat = [{ "text" : "normal, they are ambulating indepently", "score": 0},
{ "text" : "minimal currently, as they are on medical bedrest", "score": 1},
{ "text" : "very poor, they are confined to bed >72 hours", "score": 2}]

other_pmh_cat = [{ "text" : "History of inflammatory bowel disease", "score": 1},
{ "text" : "Acute MI", "score": 1},
{ "text" : "COPD", "score": 1},
{ "text" : "Present or previous malignancy", "score": 2},
{ "text" : "Other risk factors", "score": 1},
{ "text" : "BMI >25", "score": 1}]

bmi_cat = [{ "text" : "23", "score": 0},
{ "text" : "29", "score": 1}]

surgery_cat = [{ "text" : "No surgery", "score": 0},
{ "text" : "Minor surgery", "score": 1},
{ "text" : "Major >45 min, laparoscopic >45 min, or arthroscopicy", "score": 2},
{ "text" : "Elective major lower extremity arthroplasty", "score": 3}]




class Tags(Enum):
    items = "items"
    users = "users"

from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
                                                                        















                                                                                              
-                                
-                   
- 
-                                  
-                                                                           
-                                 
-                                           
-                
-                                                                    
- 






- Does the patient have active cancer (treatment or palliation within 6 months)?
- Has the patient been bedridden recently (greater than 3 days) or had major surgery within 12 weeks?
- Does the patient have calf swelling greater than 3 cm compared to the other leg? (measured 10 cm below tibial tuberosity)
- Does the patient have collateral (nonvaricose) superficial veins?
- Does that patient have an entire leg which is swollen?
- Does the patient have localized tenderness along a deep venous system?
- Does the patient have pitting edema, confined to symptomatic leg?
- Does the patient have paralysis, paresis, or recent plaster immobilization of the lower extremity?
- Does the patient have previously-documented DVT?
- Does the patient have alternative diagnosis to DVT as likely or more likely?

- active cancer 1
- bedridden recentl 1
- calf swelling 1
- collateral veins 1
- entire leg swollen 1
- localized tenderness 1
- pitting edema 1
- paralysis_paresis_or_plaster 1
- previous_dvt 1
- alternative_diagnosis_as_likely -2

Yes+1



No0

Yes+1


No0

Yes+1


No0

Yes+1


No0

Yes+1


No0

Yes+1


No0

Yes+1


No0

Yes+1
