import os
import pandas as pd
# import numpy as np
# from sklearn.metrics import confusion_matrix


def check(result_path: str, ref_path: str):
    assert os.path.isdir(ref_path), " referenced direcorty do not exists"
    path: str = os.path.join(result_path, os.listdir(result_path)[0])
    json_outs: str = os.path.join(path, os.listdir(path)[0])
    name = os.path.basename(json_outs)
    json_ref = os.path.join(ref_path, name)
    assert os.path.isfile(
        json_ref
    ), f"referenced json file with name {name} do not exists"
    df_ref: pd.DataFrame = pd.read_json(json_ref)
    df_out: pd.DataFrame = pd.read_json(json_outs)
    assert df_ref.equals(
        df_out
    ), f"json {name} should be the same than the reference json"


# def scoring(label_predicted, truth_label):
#     assert len(label_predicted) == len(
#         truth_label
#     ), "predicted values and labels should have same length"
#     score: float = np.mean(label_predicted == truth_label)
#     matrix = confusion_matrix(label_predicted, truth_label)
#     return matrix, score
