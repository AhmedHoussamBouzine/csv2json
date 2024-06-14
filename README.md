# CSV to JSON Converter

This repository contains a simple Flask application that converts CSV files to JSON.

## Features

- Upload a CSV file and get the JSON data in the response.
- Saves the converted JSON data as a file on the server.

## Installation

### Clone the repository

    ```sh
    git clone https://github.com/AhmedHoussamBouzine/csv2json.git
    ```
### Install the dependencies

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Run the application

    ```sh
    python3 app.py
    ```

### Upload a CSV file

Use the following command to upload a CSV file:

    ```sh
    curl -X POST -F 'file=@path-to-you-csv-file' http://127.0.0.1:5000/upload

    ```
or you can create a frontend application to interact with the Flask API.

You will receive the JSON data in the response and you can check the `outputs` directory for the saved JSON file.
