
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from transformers import pipeline

MODEL_ID = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

classifier = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global classifier

    print("Loading Hugging Face model...")

    classifier = pipeline(
        task="text-classification",
        model=MODEL_ID,
        device=-1
    )

    print("Model is ready!")
    yield

    classifier = None


app = FastAPI(
    title="AI Sentiment Analysis API",
    description="A sentiment analysis API using Hugging Face DistilBERT",
    version="1.0.0",
    lifespan=lifespan
)


class PredictRequest(BaseModel):
    text: str = Field(min_length=1, max_length=2000)

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Text cannot be empty")

        return value


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Sentiment Analysis API",
        "model": MODEL_ID,
        "documentation": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy" if classifier is not None else "unavailable",
        "model_loaded": classifier is not None
    }


@app.post("/predict")
def predict(request: PredictRequest):
    if classifier is None:
        raise HTTPException(
            status_code=503,
            detail="Model is not available"
        )

    try:
        result = classifier(
            request.text,
            truncation=True
        )[0]

        return {
            "input_text": request.text,
            "sentiment": result["label"],
            "confidence": round(float(result["score"]), 4)
        }

    except Exception as error:
        print(f"Prediction error: {error}")

        raise HTTPException(
            status_code=500,
            detail="Model inference failed"
        ) from error
