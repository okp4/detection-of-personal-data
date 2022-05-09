from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import MarianTokenizer, MarianMTModel
import time
import torch


class model_translate:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if model_translate.__instance is None:
            model_translate.__instance = super(model_translate, cls).__new__(cls, *args, **kwargs)
        return model_translate.__instance

    def get_models(self, src="fr", trg="en"):
        model_dt = AutoModelForSequenceClassification.from_pretrained("papluca/xlm-roberta-base-language-detection")
        tokenizer_dt = AutoTokenizer.from_pretrained("papluca/xlm-roberta-base-language-detection")
        model_name = f"Helsinki-NLP/opus-mt-{src}-{trg}"
        model = MarianMTModel.from_pretrained(model_name)
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        return tokenizer_dt, model_dt, tokenizer, model


def detect_language(text):
    tokenizer_dt, model_dt, tokenizer, model = model_translate().get_models()
    inputs = tokenizer_dt(text, return_tensors="pt")
    with torch.no_grad():
        logits = model_dt(**inputs).logits

    predicted_class_id = logits.argmax().item()
    return model_dt.config.id2label[predicted_class_id]


def translate(text):
    tokenizer_dt, model_dt, tokenizer, model = model_translate().get_models()
    time.sleep(1)
    src = detect_language(text)
    if src == "en":
        return text
    else:
        sample_text = text
        batch = tokenizer([sample_text], return_tensors="pt")
        generated_ids = model.generate(**batch)
        result = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return result
