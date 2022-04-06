from personal_data_detection import __version__
import pandas as pd
# import os
from pii import count_labels
import unittest
import sys

sys.path.append("..")


class TestMyApp(unittest.TestCase):

    def test_version(self):
        self.assertEqual(__version__, '0.1.0')


if __name__ == '__main__':
    unittest.main()
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
