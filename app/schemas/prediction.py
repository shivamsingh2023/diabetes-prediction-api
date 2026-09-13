from typing import Annotated

from pydantic import BaseModel, Field


class UserInput(BaseModel):

    Glucose: Annotated[
        float,
        Field(
            ...,
            gt=0,
            lt=300,
            description="Glucose level in mg/dL"
        )
    ]

    BloodPressure: Annotated[
        float,
        Field(
            ...,
            gt=0,
            lt=200,
            description="Blood pressure in mmHg"
        )
    ]

    BMI: Annotated[
        float,
        Field(
            ...,
            gt=0,
            lt=100,
            description="Body Mass Index"
        )
    ]

    DiabetesPedigreeFunction: Annotated[
        float,
        Field(
            ...,
            gt=0,
            lt=2.5,
            description="Diabetes pedigree function"
        )
    ]

    Age: Annotated[
        int,
        Field(
            ...,
            gt=0,
            lt=120,
            description="Age in years"
        )
    ]


class PredictionResponse(BaseModel):

    prediction: int
    result: str
    probability: float