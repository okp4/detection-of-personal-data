import pandas as pd
import os
from pii import *
os.chdir(os.getcwd() + '/src/')
# exec(open("pii.py").read())
#cities = list(set(pd.read_csv("src/cities_.csv").dropna()['0'].values))

print('')
print('test_df = pd.read_csv("test_file_small_sample.csv")')
test_df = pd.read_csv("test_file_small_sample.csv")
print('pii_res = count_labels(test_df)')
pii_res = count_labels(test_df)
print('pii_res')
print(pii_res)
print('')

print('')
print("test_df = pd.DataFrame({'Mon nom est Laval JACQUIN, j'ai 38 ans, j'habite 29 bis chemin de Rivals, \
 mon numéro de téléphone est le +33652105579 et la plaque d'immatriculation de ma voiture est BP-152-FX})")
test_df = pd.DataFrame({"Mon nom est Laval JACQUIN, j'ai 38 ans, j'habite 29 bis chemin de Rivals, \
 mon numéro de téléphone est le +33652105579 et la plaque d'immatriculation de ma voiture est BP-152-FX"})
print('pii_res = count_labels(test_df)')
pii_res = count_labels(test_df)
print('pii_res')
print(pii_res)
print('')


