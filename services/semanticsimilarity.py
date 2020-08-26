import torch
import numpy as np
from transformers import (RobertaTokenizer, RobertaForSequenceClassification, InputExample,
                          glue_convert_examples_to_features)

from services.service import Service

class SemanticSimilarity():

    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer


class SemanticSimilarityService(Service):

    def __init__(self, model_dir):
        self.model_dir = model
        self.tokenizer = RobertaTokenizer.from_pretrained(self.model_dir)
        self.model = RobertaForSequenceClassification.from_pretrained(self.model_dir)

    def get_similarity_with_concept(self, text, concept):
        example = InputExample(guid='0', text_a=text, text_b=concept)
        feature = glue_convert_examples_to_features(examples=[example],
                                                    tokenizer=self.tokenizer,
                                                    max_length=128,
                                                    output_mode='regression',
                                                    label_list=[None])

        input_ids = torch.tensor(feature[0].input_ids).unsqueeze(0)
        attention_mask = torch.tensor(feature[0].attention_mask).unsqueeze(0)

        with torch.no_grad():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)

        return outputs[0].item()

    def get_similarity_with_concepts(self, text, concepts):
        examples = [InputExample(guid='0', text_a=text, text_b=concept) for concept in concepts]
        features = glue_convert_examples_to_features(examples=examples,
                                                     tokenizer=self.tokenizer,
                                                     max_length=128,
                                                     output_mode='regression',
                                                     label_list=[None])

        input_ids = torch.tensor([feature.input_ids for feature in features])
        attention_mask = torch.tensor([feature.attention_mask for feature in features])

        with torch.no_grad():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
            outputs = outputs[0].T.tolist()[0]

        return outputs