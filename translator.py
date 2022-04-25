from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import MarianTokenizer, MarianMTModel

import torch


def detect_language(text):
    tokenizer = AutoTokenizer.from_pretrained("papluca/xlm-roberta-base-language-detection")

    model = AutoModelForSequenceClassification.from_pretrained("papluca/xlm-roberta-base-language-detection")

    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    return model.config.id2label[predicted_class_id]

def translate(text):
    trg="en"
    src= detect_language(text)
    model_name = f"Helsinki-NLP/opus-mt-{src}-{trg}"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    sample_text = text
    batch = tokenizer([sample_text], return_tensors="pt")

    generated_ids = model.generate(**batch)
    result =tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return result
