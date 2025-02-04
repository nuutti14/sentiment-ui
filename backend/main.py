from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import requests
import os
from dotenv import load_dotenv
import requests
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware
# Initialize FastAPI app
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all frontend URLs (change to your frontend URL for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Load sentiment analysis model from Hugging Face
custom_model = pipeline("text-classification", model="nutukoira/distilbert_sentiment_model")

# Groq API details
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = "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"

# Request model
class SentimentRequest(BaseModel):
    text: str
    model: str 

# Response model
class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float

@app.post("/analyze", response_model=SentimentResponse)
def analyze_sentiment(request: SentimentRequest):
    text = request.text
    model_type = request.model.lower()

    if model_type == "custom":
        result = custom_model(text)[0]
        if result["label"] == "LABEL_1":
            sentiment = "Positive"
        else:
            sentiment = "Negative"
        confidence = result["score"]

    elif model_type == "llama":
        client = Groq(api_key=GROQ_API_KEY)
        
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Classify the sentiment of this text as positive or negative in one word."
            },
            {
                "role": "user",
                "content": f"Analyze sentiment: {text}",
            }
        ],
        model="llama-3.3-70b-versatile",
            )

        sentiment = chat_completion.choices[0].message.content
        confidence = 0.9
        

    else:
        raise HTTPException(status_code=400, detail="Invalid model type. Use 'custom' or 'llama'.")

    return SentimentResponse(sentiment=sentiment, confidence=confidence)


# Run FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


