import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_DIR = os.getenv("MODEL_DIR")

class JudgeModel:
    def __init__(self, model_dir = MODEL_DIR):
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_dir)
        self.model.eval()

    def score(self, prompt, respA, respB):
        text = (
            "<|prompt|>\n" + str(prompt) + "\n\n"
            "<|response_a|>\n" + str(respA) + "\n\n"
            "<|response_b|>\n" + str(respB)
        )

        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.softmax(outputs.logits, dim=1).flatten().tolist()

        return {
            "winner_model_a": float(probs[0]),
            "winner_model_b": float(probs[1]),
            "winner_tie":     float(probs[2])
        }

judge = JudgeModel()
