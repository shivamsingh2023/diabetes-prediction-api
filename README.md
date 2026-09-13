# Diabetes Prediction API

A production-ready FastAPI application that uses a Machine Learning model to predict the probability of diabetes based on patient health parameters.

## Features

- FastAPI REST API
- Pydantic input validation
- Machine Learning prediction
- Prediction probability
- Health check endpoint
- Automated API testing
- Docker support
- Swagger API documentation
- Modular project architecture

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pandas
- Scikit-learn
- Uvicorn
- Pytest
- Docker

## Project Structure

```text
diabetes-prediction-api/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── models/
│   └── model.pkl
│
├── tests/
│   └── test_api.py
│
├── Dockerfile
├── requirements.txt
├── run.py
└── README.md