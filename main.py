from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
app = FastAPI()

nlp_pipeline = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str


@app.get("/")
async def root():
    return {"message": "Welcome to Hugging Face API with FastAPI"}

@app.post("/analyze-sentiment/")
async def analyze_sentiment(input: TextInput):
    try:
        # Sử dụng pipeline để phân tích cảm xúc
        result = nlp_pipeline(input.text)
        return {"text": input.text, "sentiment": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))