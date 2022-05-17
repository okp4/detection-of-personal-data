import numpy as np
import re
import logging
from common_regex import CommonRegex


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
Driving_license: list = ["driving license", "code"]
social_security_number: list = ["social security number"]
Tax_file_number: list = ["tax file number"]
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
    + Driving_license
    + social_security_number
    + Tax_file_number
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
    (Driving_license, "Driving_license"),
    (social_security_number, "social_security_number"),
    (Tax_file_number, "Tax_file_number"),
    (credit_card, "credit_card"),
    (persons, "persons"),
]


def predict(
    pipeline,
    sentence: str,
    threshold: float,
) -> int:
    """Documentation:
    inputs:
            pipeline: Hugging face pipeline object
            sentence : the sentence we want to predict the label
            threshold : the minimum probability of the predicted label
    This function predicts whether the sentence contains sensory information and returns a boolean value
    """
    result_details = pipeline(sentence, candidate_labels, multi_label=True)
    result_details: dict = dict(zip(result_details["labels"], result_details["scores"]))
    result: dict = {
        name: round(np.mean(list(map(result_details.get, lst))), 2)
        for lst, name in pii_
    }
    pii_detected: dict = {name: result[name] for name in thresh(result, threshold)}
    pii_detected: dict = check(pii_detected, sentence)
    if license_plate(sentence):
        pii_detected["license_plate"] = 0.99
    detected = int(pii_detected != {})
    if findMail(sentence):
        pii_detected["mail"]=0.99
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


def findBirthday(text: str) -> list:
    """Documentation:
    This function returns True if the birthday pattern was detected in the text.
    """
    p1: list = [y.group(0) for y in re.compile(r"\d{4}").finditer(text)]
    p2: list = [y.group(0) for y in re.compile(r"\d{2}").finditer(text)]
    return (p1 and p2) != []

def findMail(text: str) -> list:
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


def thresh(detected_labels: dict, treshold: float) -> list:
    """Documentation:
    inputs:
        detected_labels: detected labels and their probability
        treshold: the minimum probability of private data
    This function only takes into account the labels and their probability that satisfy the condition (probability is higher than the threshold).
    """
    result: list = [
        key
        for key, value in detected_labels.items()
        if value > treshold
        and key
        not in ("Driving_license", "", "mail", "phone", "passport", "birth", "persons")
    ]
    result += [
        key
        for key, value in detected_labels.items()
        if value > 0.8
        and key in ("person", "mail", "phone", "birth", "persons")
    ]
    result += [
        key
        for key, value in detected_labels.items()
        if value > 0.6 and key in ("Driving_license","passport")
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
        elif key == "Driving_license":
            if findNumber(text):
                print("Driving_license checked")
                pass
            else:
                result_dict.pop("Driving_license")
        elif key == "credit_card":
            if findNumber(text):
                print("credit_card checked")
                pass
            else:
                result_dict.pop("credit_card")
        elif key == "Tax_file_number":
            if findNumber(text):
                print("Tax_file_number checked")
                pass
            else:
                result_dict.pop("Tax_file_number")
        elif key == "birth":
            if findBirthday(text):
                print("birth checked")
                pass
            else:
                result_dict.pop("birth")
    return result_dict
