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


if __name__ == "__main__":
    print("you've reached this message in error")