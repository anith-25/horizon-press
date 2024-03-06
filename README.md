# Django Application with Hugging Face Transformers

This Django application is designed to accept text input from users and perform sentiment analysis as well as categorization using Hugging Face's transformers package. The application utilizes Hugging Face's models for processing text data.

## Features

1. **Sentiment Analysis**: The application leverages the pipeline module from the transformers package to identify whether the input text sentiment is positive or negative.

2. **Text Categorization**: The application categorizes the input text based on predefined categories stored in the database. This allows for flexible classification of text data.

## Installation

1. Clone the repository:

git clone https://github.com/anith-25/horizon-press.git

2. Install the required dependencies:

pip install -r requirements.txt

3. Run Django migrations to set up the database:

python manage.py migrate

4. Start the Django development server:

python manage.py runserver


5. Access the application through your web browser at `http://localhost:8000`.

## Usage

1. Enter the text you want to analyze in the provided input field.

2. Click on the "Submit" button to initiate the analysis.

3. The application will display the text under the corresponding category it falls under and the text will be displayed in a coloured card corresponding to the sentiment analysis result (green for positive and red for negative).

## Dependencies

- Django: Web framework for building the application.
- Transformers: Python library for natural language processing using pre-trained models from Hugging Face.
- Database (SQLite): For storing categories and other necessary data.

## Acknowledgements

- [Hugging Face](https://huggingface.co/): For providing state-of-the-art natural language processing models and tools.


