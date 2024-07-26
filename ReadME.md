# Data Analytics Tool

## Overview
This project aims to create a data analytics tool that sends feedback forms to multiple users, collects the data, and performs predictive analytics. The tool leverages Django REST Framework (DRF) for the backend, TensorFlow and GPT-2 for feature extraction, and a custom model for predictive analytics.

## Features
- **Feedback Form Distribution**: Send feedback forms to users.
- **Data Collection**: Collect responses from users.
- **Feature Extraction**: Use GPT-2 for extracting features from text data.
- **Predictive Analytics**: Analyze the collected data to make predictions.

## Technologies Used
- **Backend**: Django REST Framework (DRF)
- **Machine Learning**: TensorFlow, GPT-2
- **Predictive Analytics**: Custom model built with TensorFlow

## Getting Started

### Prerequisites
- Python 3.8+
- Django 3.0+
- Django REST Framework
- TensorFlow
- Transformers (Hugging Face's library)
- Other dependencies listed in `requirements.txt`

### Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/your-username/data-analytics-tool.git
    cd data-analytics-tool
    ```

2. **Create a Virtual Environment**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up Django**
    ```sh
    python manage.py migrate
    python manage.py createsuperuser
    ```

5. **Run the Server**
    ```sh
    python manage.py runserver
    ```

### Usage

#### Sending Feedback Forms
- **API Endpoint**: `/api/send-feedback`
- **Method**: POST
- **Payload**:
    ```json
    {
        "user_ids": [1, 2, 3],
        "form_id": 1
    }
    ```

#### Collecting Feedback
- **API Endpoint**: `/api/collect-feedback`
- **Method**: GET
- **Response**:
    ```json
    {
        "feedback": [
            {
                "user_id": 1,
                "response": "..."
            },
            ...
        ]
    }
    ```

#### Analyzing Data
- **API Endpoint**: `/api/analyze-data`
- **Method**: POST
- **Payload**:
    ```json
    {
        "feedback_data": [...]
    }
    ```
- **Response**:
    ```json
    {
        "predictions": [...]
    }
    ```