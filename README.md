# Sentiment Analysis and File Upload API

This project provides a Flask API for uploading `.xlsx` and `.csv` files containing customer reviews, and performing sentiment analysis on both uploaded files and individual review texts.

## Features
- **File Upload**: Accepts `.xlsx` or `.csv` files for sentiment analysis.
- **Sentiment Analysis**: Analyzes the sentiment of review texts and returns sentiment scores.

## Technologies Used
- **Flask**: A micro web framework for Python.
- **Groq API**: For sentiment analysis using a Language Learning Model (LLM).

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Flask
- `requests` library
- A valid Groq API key

### Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/trijal18/TextMoodAPI.git
    cd sentiment-analysis-api
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Required Packages**:

    ```bash
    pip install Flask requests
    ```

4. **Set Up the Groq API Key**:

    ```bash
    export GROQ_API_KEY="your-groq-api-key"  # On Windows, use `set`
    ```

5. **Run the Flask App**:

    ```bash
    python app.py
    ```

   The app will be accessible at `http://127.0.0.1:5000`.

---

## API Endpoints

### 1. Upload File API

**Endpoint**: `/upload-file`  
**Method**: `POST`  
**Description**: Upload an `.xlsx` or `.csv` file containing customer reviews for sentiment analysis.

#### Request Parameters:
- `file`: The uploaded `.xlsx` or `.csv` file.

#### Response:
- **Success (200)**:  
    ```json
    {
        "negative": score,
        "neutral": score,
        "positive": score
    }
    ```
- **Error (400)**:  
    ```json
    {
        "error": "Invalid file format. Please upload an XLSX or CSV file."
    }
    ```
- **Error (500)**:  
    ```json
    {
        "error": "An error occurred during file processing."
    }
    ```

#### Example - Using Postman:
1. Open Postman and select `POST`.
2. Use the URL: `http://127.0.0.1:5000/upload-file`.
3. In the `Body` tab, select `form-data`.
4. Add a new field named `file` and upload your `.xlsx` or `.csv` file.
5. Click `Send`.

#### Example - Using cURL:
```bash
curl -X POST -F "file=@path_to_your_file/customer_reviews.xlsx" http://127.0.0.1:5000/upload-file
```
#### Example - Using requests(python):
setup and run example.py file provided
