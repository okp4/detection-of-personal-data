import pandas as pd
import nltk
import re
from common_regex import CommonRegex
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s ', level=logging.INFO)

cities = list(set(pd.read_csv("./src/cities_.csv").dropna()['0'].values))


def args_2_para(args):
    """Documentation:
    inputs:
            args: arguments of argparser
    this function retrieves the parameters of the Argparser
    """
    logging.info('start getting parameters')
    file : str = args.input_file
    out_dir : str = args.output_dir
    overwrite : str = args.overwrite
    dry_run: bool = args.d

    return file, out_dir, overwrite, dry_run


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


grammar = """
        LC: {<NNP>*<CD><NN|NNP|NNS|JJ|NNPS|DT|CC|TO|RB|,|.>{2}(<NN|NNP|NNS|NNPS|JJ|IN|DT|CC|TO|RB|,|.>+<CD>?<NNP>*)*.*}
"""


def license_plate(text : str) -> list:
    license_plate = []
    for m in re.finditer(r"[A-Z]{2}[-][0-9]{3}[-][A-Z]{2}", text):
        license_plate.append(m.group(0))
    return license_plate


def phone_number(text: str) -> list:
    phone_number = []
    for m in re.finditer(r"((((\+|00)(\d{2}|\d{3}))[-.\s]?\d[-.\s]?)|(?:\d{2}[-.\s]?))(\d{2}[-.\s]?){4} ", text):
        phone_number.append(m.group(0)[:-1])
    return phone_number


def findPeople(s: str) -> list:
    p1 = [x.group(0) for x in re.compile(r"(mr|dr|mrs|dr|jr|sir|Mlle|Mme|M|Mr|M|Dr|mme|Sir|Jr|Mrs|name is|nom est|prenom est|(he|He) is|(she|She) is|(elle|Elle) est|(Il|il) est)(.|\s)([A-Z]\w+( [A-Z]\w+)+)").finditer(s)]
    p2 = [y.group(0) for y in re.compile(r"( [A-Z]\w+)+? [A-Z]\w+ (is|est|a)").finditer(s)]
    return p1 + p2


def funct_(sent: str):
    for w in sent:
        try:
            if w in cities:
                return sent
        except Exception:
            pass
    return None


def pii(txt : str) -> dict:
    try:
        text_labelised = {}
        persons = findPeople(txt)
        parsed_text = CommonRegex(txt)
        sent = preprocess(txt)
        cp = nltk.RegexpParser(grammar)
        cs = cp.parse(sent)
        if len(license_plate(txt)) != 0:
            text_labelised["license_plate"] = license_plate(txt)
        phones = list(set(phone_number(txt) + parsed_text.phones + parsed_text.phones_with_exts))
        if len(phones) != 0:
            text_labelised["phones"] = phones
        if len(parsed_text.emails) != 0:
            text_labelised["emails"] = parsed_text.emails
        if len(persons) != 0:
            text_labelised["Person"] = persons
        text_labelised_loc = [list(zip(*br.leaves()))[0] for br in cs.subtrees()][1:]
        text_labelised_loc = [funct_(loc) for loc in text_labelised_loc if funct_(loc) is not None]
        if len(text_labelised_loc) != 0:
            text_labelised['Adresse'] = text_labelised_loc
        return text_labelised
    except Exception:
        pass


def labs_df(df: pd.DataFrame) -> list:
    dict_label = []
    for col in df.columns:
        dict_label += [df[col].apply(pii)]
    return dict_label


def count_labels(df: pd.DataFrame) -> dict:
    dict_label = {}
    for col in df.columns:
        labels = df[col].apply(pii)
        try:
            for lab in labels:
                for key in lab.keys():
                    if key in dict_label:
                        dict_label[key] += 1
                    else:
                        dict_label[key] = 1
        except Exception :
            pass
    return dict(sorted(dict_label.items(), key=lambda item: -item[1]))