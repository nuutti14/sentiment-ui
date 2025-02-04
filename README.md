for backend:
pip install fastapi
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import requests
import os
from dotenv import load_dotenv
import requests
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

for frontend:
pip install axios
import React, { useState } from "react";
import axios from "axios";

run the api locally: 
custom:
custom_model = pipeline("text-classification", model="nutukoira/distilbert_sentiment_model")
request.model
llama with groq:
model_type == "llama":
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
