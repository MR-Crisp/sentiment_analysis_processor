# Sentiment Analysis Processor

Aim of this project is to try and use machine learning to do sentiment analysis on different phrases. 

## Features

- FastAPI-based REST API for sentiment analysis
- Linear SVC (Support Vector Classifier) machine learning model
- TF-IDF vectorization for text processing
- Docker support for easy deployment
- Trained on Twitter tweets dataset

## Quick Start with Docker

### Prerequisites
- Docker installed on your system

### Running the Application

1. **Build the Docker image:**
   ```bash
   docker build -t sentiment-analysis .
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 sentiment-analysis
   ```

3. **Access the API:**
   - API Root: http://localhost:5000
   - Interactive API docs: http://localhost:5000/docs
   - Sentiment endpoint: POST to http://localhost:5000/model

### Example API Usage

```bash
curl -X POST "http://localhost:5000/model" \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this project!"}'
```

Response:
```json
{
  "text": "I love this project!",
  "sentiment_val": 0.95,
  "sentiment": "positive"
}
```

## Local Development

### Prerequisites
- Python 3.12
- pip

### Setup

1. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   cd backend
   uvicorn main:app --reload --port 5000
   ```

## Project Plan

### Phase 1 (Completed)

In this phase, we created the basic logic for the model. We trained the model on a dataset that contains Twitter tweets, where the sentiment of each tweet is included for training. Then we used a test dataset to see how accurate the model is. At this phase, we did not worry about double negation and sarcasm as well as advanced literary techniques, but just tried to get a basic prototype working.

### Phase 2 (In Progress)

In this phase we plan to build a speech-to-text module, by connecting a microphone and running speech recognition, then running it through the sentiment analysis. I also intend on building the microphone from scratch using circuits and components if given enough time. For this section I want to use my Arduino Uno to act as an actuator to make it possible. In addition to that, in this section I will also aim to add a front end to connect to the API, this will most likely be done in React.

### Phase 3 (Future)

In this phase we will improve the basic model, trying to make it more accurate, now taking into account double negatives and sarcasm. We will also make it so that the speech-to-text analysis considers intonation, tone and other things to help feed the model information to make better judgements.

## Project Structure

## Technologies Used

- **Python 3.12** - Programming language
- **FastAPI** - Web framework for building APIs
- **scikit-learn** - Machine learning library (Linear SVC)
- **Docker** - Containerization

