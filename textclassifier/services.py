from transformers import pipeline


sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")


def analyze_sentiment(sentence: str):
    return sentiment_pipeline(sentence)[0]["label"]
    

def classify_to_categories(sentence: str, categories: list):
    return classifier(sentence, categories)["labels"][0]