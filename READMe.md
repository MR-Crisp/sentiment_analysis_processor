# Sentiment Analysis Processor

A full-stack machine learning application that analyzes the sentiment of text using a trained Linear SVC model. Features a FastAPI backend and React frontend, fully containerized with Docker.

## Features

- **Machine Learning Model**: Linear SVC (Support Vector Classifier) with TF-IDF vectorization
- **REST API**: FastAPI-based backend with automatic interactive documentation
- **Interactive UI**: React-based frontend with real-time sentiment analysis
- **Containerized**: Complete Docker Compose setup for one-command deployment
- **Production Ready**: Nginx-served frontend, optimized build process
- **Trained on Twitter Dataset**: Model trained on real-world social media data

## Frontend view
  <img width="1920" height="953" alt="image" src="https://github.com/user-attachments/assets/62b997ff-a511-4a8f-8c58-1d2ad557f906" />

## Quick Start with Docker Compose (Recommended)

### Prerequisites
- Docker and Docker Compose installed on your system

### Running the Full Application

1. **Clone the repository and navigate to project root:**
   ```bash
   cd sentiment_analysis_processor
   ```

2. **Start both frontend and backend:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   - **Frontend UI**: http://localhost:3000
   - **Backend API**: http://localhost:5000
   - **API Documentation**: http://localhost:5000/docs

4. **Stop the application:**
   ```bash
   docker-compose down
   ```
   Or press `Ctrl+C` if running in foreground

## Example of Query
<img width="1920" height="953" alt="image" src="https://github.com/user-attachments/assets/b627cc1b-0aff-4ea1-8d33-5073c27e5439" />

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

## Project Roadmap

### Phase 1: Machine Learning Model Development  (Completed)

Developed and trained a sentiment analysis model using scikit-learn's Linear Support Vector Classifier (SVC) with TF-IDF vectorization. The model was trained on a Twitter dataset containing labeled sentiment data and validated using a separate test dataset. Achieved baseline accuracy for binary sentiment classification (positive/negative).

**Key Achievements:**
- Implemented data preprocessing pipeline
- Trained Linear SVC model with TF-IDF features
- Model serialization for production deployment
- Performance evaluation and testing

### Phase 2: Full-Stack Application Development  (Completed)

Built a complete production-ready full-stack application with modern architecture:

**Backend:**
- RESTful API using FastAPI
- Pydantic models for request/response validation
- CORS configuration for cross-origin requests
- Model inference endpoint with confidence scores
- Interactive API documentation (Swagger UI)

**Frontend:**
- React single-page application
- Modern UI with London Spitfire theme
- Real-time sentiment analysis
- State management with React Hooks
- Axios for API communication
- Responsive design with custom CSS

**DevOps:**
- Complete Docker containerization
- Docker Compose for multi-container orchestration
- Nginx for production frontend serving
- Multi-stage Docker builds for optimization
- Environment-based configuration

### Phase 3: Advanced Features (Future)

**Model Enhancements:**
- Advanced NLP techniques for handling double negatives
- Sarcasm detection using contextual analysis
- Improved accuracy with ensemble methods or deep learning
- Multi-class sentiment (positive, negative, neutral, mixed)


## Technologies Used

### Backend
- **Python 3.12** - Programming language
- **FastAPI** - Modern web framework for building APIs
- **scikit-learn** - Machine learning library (Linear SVC)
- **TF-IDF** - Text vectorization technique
- **Pydantic** - Data validation using Python type hints
- **Uvicorn** - ASGI server for FastAPI
- **Joblib** - Model serialization

### Frontend
- **React 18** - JavaScript library for building user interfaces
- **JavaScript (ES6+)** - Programming language
- **Node.js & npm** - JavaScript runtime and package manager


## Model Information

The sentiment analysis uses a **Linear Support Vector Classifier (SVC)** trained on Twitter data:

- **Algorithm**: Linear SVC (Support Vector Machine for classification)
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Output**: Binary sentiment classification (positive/negative)
- **Confidence Score**: Returns probability estimate for the prediction
- **Training Data**: Twitter tweets with labeled sentiment

## API Endpoints

### `POST /model`
Analyzes sentiment of provided text.

**Request Body:**
```json
{
  "text": "Your text to analyze"
}
```

**Response:**
```json
{
  "text": "Your text to analyze",
  "sentiment": "positive",
  "sentiment_val": 0.85
}
```

**Fields:**
- `text`: The analyzed text
- `sentiment`: Classification result ("positive" or "negative")
- `sentiment_val`: Confidence score (0.0 to 1.0)
