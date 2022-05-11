from functions import pii_detect
import pandas as pd
df=pd.read_csv('/Users/nour/Documents/OKP4/detection-of-personal-data/data_test/personal_data_db_translated.csv')
df=df.dropna()
res= pii_detect(df)
print(res)