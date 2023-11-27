# MELD-Na

### About
The MELD-Na calculator is an evolution of the Model for End-Stage Liver Disease (MELD) scoring system. The original MELD score was developed to predict mortality within three months of surgery in patients who had undergone a transjugular intrahepatic portosystemic shunt (TIPS) procedure. It was found to be an effective tool for determining the prognosis and prioritizing patients for liver transplant.

Recognizing its accuracy in predicting short-term survival among patients with cirrhosis, the United Network for Organ Sharing (UNOS) adopted MELD in 2002 for prioritizing patients awaiting liver transplantation in the United States. MELD is a prognostic score that measures the severity of liver failure to estimate short-term survival in patients with chronic liver disease.

The original MELD calculator used measurements of creatinine, bilirubin, and INR. It was later discovered that hyponatremia (low sodium concentration in the blood) was an independent predictor of mortality in patients with cirrhosis. Consequently, sodium levels were integrated into the MELD score to improve its predictive accuracy, leading to the creation of the MELD-Na score. This new scoring system, MELDNa, includes the serum sodium parameter to account for the added risk of significant hyponatremia. The MELD-Na calculator thus became a more comprehensive tool for assessing the severity of liver disease and the urgency of liver transplantation.

The **MELD-Na calculator** is designed to:

- Calculate the Model for End-Stage Liver Disease (MELD) score, integrating serum sodium levels.
- Provide a measure of the severity of liver disease.
- Aid in determining the priority for liver transplantation based on medical urgency for patients aged 12 and older.
- Account for the added risk of significant hyponatremia, which is linked to mortality in cirrhosis patients.

MELD scores, which the calculator determines, range from 6 to 40. A higher MELD score signifies a greater risk of 3-month mortality due to liver disease.

### Constraints

- If the sodium level is less than 125 mmol/L, it is set to 125 mmol/L to avoid over-penalization.
- If the sodium level is greater than 137 mmol/L, it is set to 137 mmol/L to avoid over-credit.
- Laboratory values less than 1.0 for the components of the MELD score are set to 1.0 to prevent generating a negative score.

### Parameters

The MELD-Na calculation uses the following laboratory values:

- `Creatinine` (mg/dL)
- `Bilirubin` (mg/dL)
- `INR` (International Normalized Ratio)
- `Serum Sodium` (mmol/L)

### Notes

- This score is used for patients above the age of 12 years.
- The calculator includes United Network for Organ Sharing (UNOS) modifications of the original model.

### References:
- Kamath PS, Wiesner RH, Malinchoc M, Kremers W, Therneau TM, Kosberg CL, D'Amico G, Dickson ER, Kim WR. A model to predict survival in patients with end-stage liver disease. Hepatology. 2001 Feb;33(2):464-70. Available at: [Pubmed](https://www.ncbi.nlm.nih.gov/pubmed/11172350).
- Kamath PS, Kim WR; Advanced Liver Disease Study Group. The model for end-stage liver disease (MELD). Hepatology. 2007 Mar;45(3):797-805. Available at: [Pubmed](https://www.ncbi.nlm.nih.gov/pubmed/17326206).
- Wiesner R, Edwards E, Freeman R, Harper A, Kim R, Kamath P, Kremers W, Lake J, Howard T, Merion RM, Wolfe RA, Krom R; United Network for Organ Sharing Liver Disease Severity Score Committee. Model for end-stage liver disease (MELD) and allocation of donor livers. Gastroenterology. 2003 Jan;124(1):91-6. Available at: [Pubmed](https://www.ncbi.nlm.nih.gov/pubmed/12512033).
- [GlobalRPH](https://globalrph.com/medcalcs/meld-na-score-model-for-end-stage-liver-disease/)
- [Stanford University MedCalculators](medcalculators.stanford.edu)
- [OPTN](optn.transplant.hrsa.gov)
