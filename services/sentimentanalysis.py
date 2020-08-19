import torch
import numpy as np
from transformers import (DistilBertTokenizer, DistilBertForSequenceClassification)

from services.service import Service


class SentimentClassifier:

    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    def __call__(self, text):
        input_ids = torch.tensor(self.tokenizer.encode(text, add_special_tokens=True)).unsqueeze(0)
        outputs = self.model(input_ids)
        outputs = outputs[0].detach().numpy()
        scores = np.exp(outputs) / np.exp(outputs).sum(-1)
        scores = scores[0].tolist()
        result = {"negative": scores[0], "neutral": scores[1], "positive": scores[2]}
        return result

class SentimentAnalysisService(Service):
    '''
    This is heavy service that can be run locally and WONT be instantiated for each new
    user that connects to the system, it's a singleton service
    '''
    def __init__(self, config):
        super().__init__(config)
        self.url = config["url"]
        self.tokenizer = DistilBertTokenizer.from_pretrained(self.url)
        self.model = DistilBertForSequenceClassification.from_pretrained(self.url)

    def get_sentiment(self, text):
        sentiment_classifier = SentimentClassifier(self.model, self.tokenizer)
        result = sentiment_classifier(text)
        sentiment = max(result, key=result.get)
        print("sentiment of {}: {}".format(text, sentiment))
        return sentiment