from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import MarianTokenizer, MarianMTModel
import time
import torch


trg="en"
src = "fr"
model_dt = AutoModelForSequenceClassification.from_pretrained("papluca/xlm-roberta-base-language-detection")
tokenizer_dt = AutoTokenizer.from_pretrained("papluca/xlm-roberta-base-language-detection")
model_name = f"Helsinki-NLP/opus-mt-{src}-{trg}"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)


def detect_language(text):
    inputs = tokenizer_dt(text, return_tensors="pt")
    with torch.no_grad():
        logits = model_dt(**inputs).logits

    predicted_class_id = logits.argmax().item()
    return model_dt.config.id2label[predicted_class_id]



def translate(text):
    time.sleep(1)
    # trg="en"
    src= detect_language(text)
    if src == "en":
        return text
    sample_text = text
    batch = tokenizer([sample_text], return_tensors="pt")
    generated_ids = model.generate(**batch)
    result =tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return result
