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