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

    def get_model_lang_detect(self):
        model_lang_detect = AutoModelForSequenceClassification.from_pretrained("papluca/xlm-roberta-base-language-detection")
        tokenizer_lang_detect = AutoTokenizer.from_pretrained("papluca/xlm-roberta-base-language-detection")
        return tokenizer_lang_detect, model_lang_detect

    def get_model_trans(self, src="fr", trg="en"):
        model_name_trans = f"Helsinki-NLP/opus-mt-{src}-{trg}"
        model_trans = MarianMTModel.from_pretrained(model_name_trans)
        tokenizer_trans = MarianTokenizer.from_pretrained(model_name_trans)
        return tokenizer_trans, model_trans


def detect_language(text):
    tokenizer_lang_detect, model_lang_detect = model_translate().get_model_lang_detect()
    inputs = tokenizer_lang_detect(text, return_tensors="pt")
    with torch.no_grad():
        logits = model_lang_detect(**inputs).logits
    predicted_class_id = logits.argmax().item()
    return model_lang_detect.config.id2label[predicted_class_id]


def translate(text):
    tokenizer_trans, model_trans = model_translate().get_model_trans()
    time.sleep(1)
    src = detect_language(text)
    if src == "en":
        return text
    else:
        sample_text = text
        batch = tokenizer_trans([sample_text], return_tensors="pt")
        generated_ids = model_trans.generate(**batch)
        result = tokenizer_trans.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return result
