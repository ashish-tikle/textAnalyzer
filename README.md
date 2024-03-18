# Document Analyzer

This project provides a Python application for analyzing text documents stored in Google Cloud Storage.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/document-analyzer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd document-analyzer
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Before running the application, make sure to set up authentication for Google Cloud Storage. You can follow the official documentation for guidance on setting up authentication: https://cloud.google.com/docs/authentication

## Usage

1. Modify `main.py` to specify the name of your Google Cloud Storage bucket.

2. Build the Docker image:

    ```bash
    docker build -t document-analyzer .
    ```

3. Run the Docker container:

    ```bash
    docker run -d document-analyzer
    ```

