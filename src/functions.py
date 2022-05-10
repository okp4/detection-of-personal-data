from pii_translator import translate
import numpy as np
import re
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s ', level=logging.INFO)


name = ["person's name", "person"]
birth = ["birthday", "private"]
# ip=["Internet protocol (IP) addresses","IP adress"]
cookie = ["cookie identifiers", "a cookie"]
phone = ["phone numbers", "phone number", "telphone number"]
mail = ["mail addresses", "mail address", "mail"]
location = ["location adress", "private postal address"]
health = ["health data", "medical records", "health information", "medical information", "Medical Procedure names", "Medical Procedure identification codes"]
personal = ["personal data", "personal", "personal information", "private data", "private information"]
not_personal = ["not personal data", "not personal information", "not personal", "not private data", "not private", "not private information"]
passport = ['passport', 'code']
Driving_license = ['driving license', 'code']
social_security_number = ['social security number']
Tax_file_number = ['tax file number']
credit_card = ['credit card number']
candidate_labels = name + cookie + phone + mail + location + health + personal + not_personal + birth + passport + Driving_license + social_security_number + Tax_file_number + credit_card
pii_ = [(name, 'person'), (birth, 'birth'), (cookie, 'cookie'), (phone, 'phone'), (mail, 'mail'), (location, 'location'), (health, 'health'), (personal, 'personal'),
        (not_personal, 'not_personal'), (passport, "passport"), (Driving_license, "Driving_license"), (social_security_number, "social_security_number"), (Tax_file_number, "Tax_file_number"), (credit_card, "credit_card")]


def predict(pipeline, sentence : str, threshold : float):
    text_translated = translate(sentence)
    result_details = pipeline(text_translated, candidate_labels, multi_label=True)
    result_details = dict(zip(result_details['labels'], result_details['scores']))
    result = {name : np.mean(list(map(result_details.get, lst))) for lst, name in pii_}
    pii_detected = {name : result[name] for name in thresh(result, threshold)}
    pii_detected = check(pii_detected, sentence)
    if license_plate(sentence):
        pii_detected["license_plate"] = 0.9
    if pii_detected == {}:
        mean = 0
    else:
        mean = np.mean(list(pii_detected.values()))
    del text_translated, result_details, result
    return int(pii_detected != {}), mean


def license_plate(text : str) -> bool:
    license_plate = []
    for m in re.finditer(r"[A-Z]{2}[-][0-9]{3}[-][A-Z]{2}", text):
        license_plate.append(m.group(0))
    return license_plate != []


def phone_number(text: str) -> bool:
    phone_number = []
    for m in re.finditer(r"((((\+|00)(\d{2}|\d{3}))[-.\s]?\d[-.\s]?)|(?:\d{2}[-.\s]?))(\d{2}[-.\s]?){4} ", text):
        phone_number.append(m.group(0)[:-1])
    return phone_number


def findBirthday(s: str) -> list:
    p1 = [y.group(0) for y in re.compile(r"\d{4}").finditer(s)]
    p2 = [y.group(0) for y in re.compile(r"\d{2}").finditer(s)]
    return (p1 and p2) != []


def findPassport(s: str) -> bool:
    return [y.group(0) for y in re.compile(r" (?!^0+$)[a-zA-Z0-9]{9} ").finditer(s)] != []


def findSecurityNumber(s: str) -> bool:
    return [y.group(0) for y in re.compile(r"\d{13}").finditer(s)] != []


def findNumber(s: str) -> bool:
    return [y.group(0) for y in re.compile(r"\d{4}\d*").finditer(s)] != []

# def findBirthday(s: str) -> bool:
#     return [y.group(0) for y in re.compile(r"(([0-2])\d)[\/\-.](([0-2])\d)[\/\-.][19|20]\d{3}").finditer(s)] != []


def thresh(d : dict, thresh: float) -> list:
    result = [key for key, value in d.items()if value > thresh and key not in ('Driving_license', 'personal', 'not_personal')]
    result += ['Driving_license'] if d['Driving_license'] > 0.6 else []
    return result


def check(result: dict, text: str) -> dict:
    result_dict : dict = result.copy()
    for key in result.keys():
        if key == 'passport':
            if findPassport(text):
                print('passport checked')
                pass
            else:
                result_dict.pop('passport')
        elif key == 'security_number':
            if findSecurityNumber(text):
                print('security_number checked')
                pass
            else:
                result_dict.pop('security_number')
        elif key == 'Driving_license':
            if findNumber(text):
                print('Driving_license checked')
                pass
            else:
                result_dict.pop('Driving_license')
        elif key == 'credit_card':
            if findNumber(text):
                print('credit_card checked')
                pass
            else:
                result_dict.pop('credit_card')
        elif key == 'Tax_file_number':
            if findNumber(text):
                print('Tax_file_number checked')
                pass
            else:
                result_dict.pop('Tax_file_number')
        elif key == 'birth':
            if findBirthday(text):
                print('birth checked')
                pass
            else:
                result_dict.pop('birth')
    return result_dict
