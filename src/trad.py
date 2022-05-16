import pandas as pd
from tqdm import tqdm
from functions import predict
from transformers import pipeline

df = pd.read_csv(
    "/Users/nour/Documents/OKP4/detection-of-personal-data/data_test/personal_data_db_translated.csv"
)


pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
detected_labels: list = [
    predict(pipe, sent, threshold=0.9) for sent in tqdm(df["sentence"], total=len(df))
]
print(detected_labels)
