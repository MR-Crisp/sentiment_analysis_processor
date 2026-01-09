from fastapi import FastAPI
from pydantic import BaseModel


class SentimentRequest(BaseModel):
    text: str

app = FastAPI()
@app.get("/"):
def root():
    return {"message": "Hello World"}
@app.get("/model"):
def model(request: SentimentRequest):
    return {"text": request.text}
