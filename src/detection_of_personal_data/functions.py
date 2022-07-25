from typing import Tuple
import numpy as np
import re
import logging
from common_regex import CommonRegex
import os
import json


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s ",
    level=logging.INFO,
)
# classes and their subclasses to detect
name: list = ["person's name", "person", "name"]
birth: list = ["birthday"]
# ip=["Internet protocol (IP) addresses","IP adress"]
cookie: list = ["cookie identifiers", "a cookie"]
phone: list = ["phone number", "phone"]
persons: list = ["persons"]
mail: list = ["mail addresses", "mail address", "mail"]
location: list = ["location", "postal address"]
health: list = [
    "health data",
    "medical records",
    "health information",
    "medical information",
    "Medical Procedure names",
    "Medical Procedure identification codes",
]
passport: list = ["passport", "code"]
driving_licence: list = ["driving license", "code"]
social_security_number: list = ["social security number"]
tax_file_number: list = ["tax file number"]
credit_card: list = ["credit card number"]


candidate_labels: list = (
    name
    + cookie
    + phone
    + mail
    + location
    + health
    + birth
    + passport
    + driving_licence
    + social_security_number
    + tax_file_number
    + credit_card
    + persons
)


pii_: list = [
    (name, "person"),
    (birth, "birth"),
    (cookie, "cookie"),
    (phone, "phone"),
    (mail, "mail"),
    (location, "location"),
    (health, "health"),
    (passport, "passport"),
    (driving_licence, "driving_licence"),
    (social_security_number, "social_security_number"),
    (tax_file_number, "tax_file_number"),
    (credit_card, "credit_card"),
    (persons, "persons"),
]


def predict(
    pipeline,
    sentence: str,
    threshold: dict,
) -> Tuple:
    """Documentation:
    inputs:
            pipeline: Hugging face pipeline object
            sentence : the sentence we want to predict the label
            threshold : the minimum probability of the predicted label
    This function predicts whether the sentence contains sensory information and returns a boolean value
    """
    results = pipeline(sentence, candidate_labels, multi_label=True)
    result_details: dict = dict(zip(results["labels"], results["scores"]))
    result: dict = {
        name: round(np.mean(list(map(result_details.get, lst))), 2)
        for lst, name in pii_
    }
    pii_detected: dict = {name: result[name] for name in thresh(result, threshold)}
    pii_detected = check(pii_detected, sentence)
    if license_plate(sentence):
        pii_detected["license_plate"] = 0.99
    if findMail(sentence):
        pii_detected["mail"] = 0.99
    detected: int = int(pii_detected != {})
    if detected > 0:
        return (detected, pii_detected), sentence
    return None, None


def license_plate(text: str) -> bool:
    """Documentation:
    This function returns True if the license plate pattern was detected in the text.
    """
    license_plate: list = []
    for m in re.finditer(r"[A-Z]{2}[-][0-9]{3}[-][A-Z]{2}", text):
        license_plate.append(m.group(0))
    return license_plate != []


def findBirthday(text: str) -> bool:
    """Documentation:
    This function returns True if the birthday pattern was detected in the text.
    """
    p1: list = [y.group(0) for y in re.compile(r"\d{4}").finditer(text)]
    p2: list = [y.group(0) for y in re.compile(r"\d{2}").finditer(text)]
    return (p1 and p2) != []


def findMail(text: str) -> bool:
    """Documentation:
    This function returns True if the birthday pattern was detected in the text.
    """
    parsed_text = CommonRegex(text)
    return len(parsed_text.emails) != 0


def findPassport(text: str) -> bool:
    """Documentation:
    This function returns True if the passport pattern was detected in the text.
    """
    return [
        y.group(0) for y in re.compile(r" (?!^0+$)[a-zA-Z0-9]{9} ").finditer(text)
    ] != []


def findSecurityNumber(text: str) -> bool:
    """Documentation:
    This function returns True if the Security number pattern was detected in the text.
    """
    return [y.group(0) for y in re.compile(r"\d{13}").finditer(text)] != []


def findNumber(text: str) -> bool:
    """Documentation:
    This function returns True if the number pattern (at least 4 numbers) was detected in the text.
    """
    return [y.group(0) for y in re.compile(r"\d{4}.\d*").finditer(text)] != []


def thresh(detected_labels: dict, tresholds: dict) -> list:
    """Documentation:
    inputs:
        detected_labels: detected labels and their probability
        treshold: the minimum probability of private data
    This function only takes into account the labels and their probability that satisfy the condition (probability is higher than the threshold).
    """
    result: list = [
        key for key, value in detected_labels.items() if value > tresholds[key]
    ]

    if "persons" in result and "person" in result:
        result.remove("persons")
    return result


def check(result: dict, text: str) -> dict:
    """Documentation:
    inputs:
        detected_labels: detected labels and their probability
    This function checks the result of the detected labels.
    """
    result_dict: dict = result.copy()
    for key in result.keys():
        if key == "passport":
            if findPassport(text):
                print("passport checked")
                pass
            else:
                result_dict.pop("passport")
        elif key == "security_number":
            if findSecurityNumber(text):
                print("security_number checked")
                pass
            else:
                result_dict.pop("security_number")
        elif key == "driving_licence":
            if findNumber(text):
                print("driving_licence checked")
                pass
            else:
                result_dict.pop("driving_licence")
        elif key == "credit_card":
            if findNumber(text):
                print("credit_card checked")
                pass
            else:
                result_dict.pop("credit_card")
        elif key == "tax_file_number":
            if findNumber(text):
                print("tax_file_number checked")
                pass
            else:
                result_dict.pop("tax_file_number")
        elif key == "birth":
            if findBirthday(text):
                print("birth checked")
                pass
            else:
                result_dict.pop("birth")
    return result_dict


def to_json(output: dict, output_path: str, overwrite: bool) -> None:
    """Documentation:
    inputs:
            output: dict to save
            output_path : path of the directory where the json will be saved
            overwrite : 'true' to overwrite the existing json file
    this function saves the json in the directory
    """
    file_name: str = os.path.basename(output_path)
    if overwrite or not os.path.exists(output_path):
        logging.info(f"the json with name {file_name} was saved succefully")
        with open(output_path, "w") as fp:
            json.dump(output, fp)
    else:
        logging.error(f"the json with name {file_name} is duplicated")
        raise ValueError(f"{file_name} already exists")


def out(
    input_file: str,
    out_dir: str,
    file_name: str,
    detected_labels,
    dry_run: bool,
    overwrite: bool,
    to_test: bool,
):
    results = list(zip(*detected_labels))[0]
    labels = [int(elem is not None) for elem in results]
    if to_test:
        return labels

    results = list(filter(None, results))
    sentences = list(zip(*detected_labels))[1]
    sentences = list(filter(None, sentences))
    outputs_detected = {}
    detected = 0
    if results != []:
        detected = sum(list(zip(*results))[0])
        outputs_detected = {
            sent: reslt for (sent, reslt) in zip(sentences, list(zip(*results))[1])
        }
    output = {
        "FileName": os.path.basename(input_file),
        "Personal information detected": True if detected > 0 else False,
        "Results": outputs_detected,
    }
    output_path = os.path.join("./", out_dir, "sheet_" + file_name + "_result.json")
    if not dry_run:
        to_json(output, output_path, overwrite)
