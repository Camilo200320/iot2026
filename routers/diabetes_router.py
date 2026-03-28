from fastapi import APIRouter
from schemas.diabetes_schemas import PatientData,  PatientDiabetesOutput, patientDiabetesData
from services.diabetes_service import diabetes_prediction

router = APIRouter()

@router.post("/predict")
async def predict(data: patientDiabetesData):
    # prediction = "sano"
    prediction = diabetes_prediction(data)

    result = PatientDiabetesOutput(
        first_name=data.first_name,
        last_name=data.last_name,
        prediction=prediction
    )

    return {"prediction":result}


