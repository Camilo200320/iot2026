from pydantic import BaseModel

class PatientData(BaseModel):
        first_name: str
        last_name: str


class patientDiabetesData(BaseModel):
        first_name: str
        last_name: str
        pregnancies: int
        glucose: int
        bloodpresure: int
        skinthickness: int
        insulin: int
        bmi: float 
        diabetepedigreefunction: float
        age: int

class PatientDiabetesOutput(BaseModel):
        first_name: str
        last_name: str
        prediction: str


        