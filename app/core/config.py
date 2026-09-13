from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "models" / "model.pkl"

APP_NAME = "Diabetes Prediction API"
APP_VERSION = "1.0.0"