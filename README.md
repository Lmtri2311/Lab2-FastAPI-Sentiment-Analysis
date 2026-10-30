# AI Sentiment Analysis API

**Computational Thinking – Lab 2: Application Programming Interface**

## 1. Student Information

| Field | Information |
|---|---|
| Full Name | Lê Minh Trí |
| Student ID | 25127526 |
| Class | 25C09 |
| University | University of Science – VNU-HCM |
| Course | Computational Thinking |

## GitHub Repository

The complete source code is available at:

https://github.com/Lmtri2311/Lab2-FastAPI-Sentiment-Analysis

## 2. Project Overview

This project implements an AI-powered Sentiment Analysis API using **FastAPI** and a pretrained **DistilBERT model from Hugging Face**.

The application receives English text from users, analyzes its sentiment, and returns the prediction in JSON format.

The model classifies text into two categories:

- **POSITIVE:** Text expressing positive sentiment.
- **NEGATIVE:** Text expressing negative sentiment.

Each prediction includes a confidence score indicating the model's confidence in its classification.

### Main Features

- RESTful API developed using FastAPI.
- Pretrained Hugging Face model integration.
- Sentiment analysis for English text.
- JSON-formatted API responses.
- Input validation using Pydantic.
- Error handling for invalid inputs and inference failures.
- Automated API testing using Python `requests`.
- Interactive API documentation using Swagger UI.

## 3. Hugging Face Model

| Property | Description |
|---|---|
| Model | DistilBERT SST-2 |
| Model ID | `distilbert/distilbert-base-uncased-finetuned-sst-2-english` |
| Source | Hugging Face |
| Task | Text Classification / Sentiment Analysis |
| Language | English |
| Output Labels | POSITIVE / NEGATIVE |

**Model URL:**

https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

The selected model is a pretrained DistilBERT model fine-tuned on the Stanford Sentiment Treebank (SST-2) dataset.

The application uses the Hugging Face `transformers` library to load the model and perform sentiment classification.

The model runs locally on the CPU and does not require a dedicated GPU.

## 4. Technologies Used

- **Python:** Main programming language.
- **FastAPI:** Web API framework.
- **Uvicorn:** ASGI server for running FastAPI.
- **Hugging Face Transformers:** Model loading and inference.
- **PyTorch:** Deep learning framework.
- **Pydantic:** Request validation.
- **Requests:** HTTP API testing.

## 5. Project Structure

```text
lab2_FastAPI/
│
├── main.py
├── test_api.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .venv/                # Local virtual environment (excluded from Git)
```

### File Descriptions

| File | Description |
|---|---|
| `main.py` | FastAPI application, model initialization, API endpoints, validation, and error handling |
| `test_api.py` | API testing script using the requests library |
| `requirements.txt` | Python dependencies required by the project |
| `README.md` | Project documentation and usage instructions |
| `.gitignore` | Excludes unnecessary files and virtual environments from Git |

## 6. Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/Lmtri2311/Lab2-FastAPI-Sentiment-Analysis.git
cd lab2_FastAPI
```

If the cloned repository folder has a different name, navigate to that folder instead.

### Step 2: Create a Virtual Environment

Python 3.15.0 was used during development.

On Windows:

```powershell
py -3.15 -m venv .venv
```

### Step 3: Install Dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
```

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

The required libraries include FastAPI, Uvicorn, Transformers, PyTorch, and Requests.

**Note:** An Internet connection is required to download the pretrained model during the first execution.

## 7. Running the Application

Start the FastAPI server using the following command:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
```

During startup, the application automatically loads the Hugging Face model.

Expected terminal output:

```text
Loading Hugging Face model...
Model is ready!
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8000
```

After successful startup, the API is available at:

**Base URL:** http://127.0.0.1:8000

**Swagger UI:** http://127.0.0.1:8000/docs

**OpenAPI Schema:** http://127.0.0.1:8000/openapi.json

Keep the terminal running while using or testing the API.

## 8. API Endpoints

The application provides three main endpoints.

### 8.1. GET `/` – Home

**Purpose:** Returns general information about the application.

**Request:**

```http
GET http://127.0.0.1:8000/
```

**Example Response:**

```json
{
  "message": "Welcome to AI Sentiment Analysis API",
  "model": "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
  "documentation": "/docs"
}
```

### 8.2. GET `/health` – Health Check

**Purpose:** Checks whether the API and Hugging Face model are ready.

**Request:**

```http
GET http://127.0.0.1:8000/health
```

**Example Response:**

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

When `model_loaded` is `true`, the model is ready to process prediction requests.

### 8.3. POST `/predict` – Sentiment Prediction

**Purpose:** Analyzes the sentiment of English text using the pretrained model.

**Request:**

```http
POST http://127.0.0.1:8000/predict
Content-Type: application/json
```

**Request Body:**

```json
{
  "text": "I absolutely love this movie!"
}
```

**Example Response:**

```json
{
  "input_text": "I absolutely love this movie!",
  "sentiment": "POSITIVE",
  "confidence": 0.9999
}
```

### Request Parameters

| Field | Type | Required | Description |
|---|---|---|---|
| `text` | string | Yes | English text to analyze, between 1 and 2000 characters |

Whitespace-only input is not accepted.

### Response Fields

| Field | Type | Description |
|---|---|---|
| `input_text` | string | Original text after whitespace trimming |
| `sentiment` | string | Predicted sentiment: POSITIVE or NEGATIVE |
| `confidence` | float | Confidence score between 0 and 1 |

## 9. API Testing Examples

### Test Case 1: Positive Sentiment

**Input:**

```json
{
  "text": "I absolutely love this movie!"
}
```

**Example Output:**

```json
{
  "input_text": "I absolutely love this movie!",
  "sentiment": "POSITIVE",
  "confidence": 0.9999
}
```

**Expected HTTP Status:** `200 OK`

### Test Case 2: Negative Sentiment

**Input:**

```json
{
  "text": "This is the worst experience ever."
}
```

**Example Output:**

```json
{
  "input_text": "This is the worst experience ever.",
  "sentiment": "NEGATIVE",
  "confidence": 0.9998
}
```

**Expected HTTP Status:** `200 OK`

*Note: Confidence scores are model-generated values and may vary depending on the input and runtime environment.*

## 10. Input Validation and Error Handling

The API uses Pydantic to validate input data.

### Invalid Input: Empty Text

**Request:**

```json
{
  "text": ""
}
```

**HTTP Status:** `422 Unprocessable Content`

The API rejects the request because the text does not satisfy the minimum length requirement.

### Invalid Input: Missing Field

**Request:**

```json
{}
```

**HTTP Status:** `422 Unprocessable Content`

The API rejects the request because the required `text` field is missing.

### Invalid Input: Incorrect Data Type

**Request:**

```json
{
  "text": 123
}
```

**HTTP Status:** `422 Unprocessable Content`

The API rejects the request because the input is not a valid string.

### Model Error Handling

The application also handles errors that may occur during model inference.

- **503 Service Unavailable:** The model is not available.
- **500 Internal Server Error:** An error occurs during model inference.

These mechanisms help prevent unexpected failures and provide structured error responses.

## 11. Automated API Testing

The project includes `test_api.py`, which uses the Python `requests` library to test the API automatically.

Before running the tests, make sure the FastAPI server is running.

Open a second terminal and execute:

```powershell
.\.venv\Scripts\python.exe test_api.py
```

The testing script checks seven cases:

| Test | Expected HTTP Status |
|---|---|
| Home endpoint | 200 |
| Health endpoint | 200 |
| Positive sentiment | 200 |
| Negative sentiment | 200 |
| Empty text | 422 |
| Missing text | 422 |
| Invalid input type | 422 |

**Test Result:**

```text
All API tests passed!
```

All seven API test cases passed successfully during local development.

## 12. Demonstration Video

The demonstration video presents:

1. Introduction to the selected Hugging Face model.
2. Explanation of the project source code structure.
3. Instructions for running the FastAPI application.
4. API testing with positive and negative sentiment inputs.
5. Explanation of prediction results and input validation.

**Video Duration:** Maximum 5 minutes.

**Demonstration Video Link:**

[INSERT YOUR YOUTUBE OR GOOGLE DRIVE VIDEO LINK HERE]

The video will be publicly accessible or available to anyone with the shared link.

## 13. Limitations

- The selected model primarily supports English text.
- The model only predicts positive or negative sentiment.
- The API does not support neutral sentiment classification.
- The model may produce incorrect predictions for ambiguous, sarcastic, or context-dependent text.
- Model inference performance depends on the local hardware.

## 14. Conclusion

This project demonstrates how to integrate a pretrained Hugging Face model into a functional Web API using FastAPI.

Through this project, I learned how to:

- Load and use a pretrained machine learning model.
- Develop RESTful API endpoints using FastAPI.
- Validate user input using Pydantic.
- Handle API errors and return JSON responses.
- Test API functionality using Python requests.
- Organize and document a Python project for GitHub.

The resulting application provides a simple and functional API for sentiment analysis of English text.
