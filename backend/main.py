from fastapi import FastAPI
from pydantic import BaseModel,Field
from model import predict
from fastapi.middleware.cors import CORSMiddleware


class SentimentRequest(BaseModel):
    text: str = Field(...,description="Text for sentiment to be calculated on")

class SentimentResponse(BaseModel):
    text: str = Field(..., description="Text for sentiment to be calculated on")
    sentiment_val: float = Field(..., description="Sentiment value, 0 for negative, 1 for positive")
    sentiment: str = Field(..., description="The sentiment of the text")

app = FastAPI()
@app.get("/")
def root():
    return {"message": "This is my Api for the sentiment analysis"}
@app.post("/model", response_model=SentimentResponse)
def calculateSentiment(request: SentimentRequest):
    text = request.text
    sentiment, confidence = predict(text)
    return SentimentResponse(
            text=request.text,
            sentiment_val=confidence,
            sentiment=sentiment

        )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

