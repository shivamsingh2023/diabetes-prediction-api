from fastapi import APIRouter, HTTPException, status

from app.schemas.prediction import UserInput, PredictionResponse
from app.services.prediction_service import predict_diabetes


router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Diabetes Prediction API is running",
        "status": "healthy"
    }


@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@router.post(
    "/predict",
    response_model=PredictionResponse,
    status_code=status.HTTP_200_OK
)
def predict(data: UserInput):

    try:
        result = predict_diabetes(data)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Prediction failed: {str(e)}"
        )