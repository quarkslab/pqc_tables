#! /usr/bin/python3

import sys
import json

def roman_number(i):
    if i == "1":
        return "I"
    elif i == "2":
        return "II"
    elif i == "3":
        return "III"
    elif i == "4":
        return "IV"
    elif i == "5":
        return "V"
    elif i == "< 1":
        return "< I"

def format_number(i):
    if i.isdigit():
        return "{:,}".format(int(i))
    return i

# key can be: sk, pk, sig, ct, ss
def format_doc_code_data(variant, key):
    keycode = key + "code"
    if key in variant and keycode in variant :
        return format_number(variant[key]) + " / " + format_number(variant[keycode])
    elif key in variant:
        return format_number(variant[key])
    else:
        return format_number(variant[keycode])

def format_level(scheme):
    return ", ".join([roman_number(i["level"]) for i in scheme["levels"]])

# def simple_tables(data):
    # names = [scheme["name"] for scheme in data]
    # lname = max([len(i) for i in names])
    # format_name = "{0: <" + str(lname) + "}"
    # variants = []
    # for scheme in data:
        # var = []
        # for variant in scheme["variants"]:
            # if variant["levels"][-1]["level"] == "5":
                # var.append(variant["variant"])
        # variants.append(", ".join(var))
    # lvariants = max([len(i) for i in variants])
    # format_variants = "{0: <" + str(lvariants) + "}"

    # for i in range(len(names)):
        # print("| " + format_name.format(names[i]) + " | " + format_variants.format(variants[i]) + " |")

def complete_tables(data):
    for scheme in data:
        for variant in scheme["variants"]:
            s = ""
            if scheme["scheme"] == "KEM":
                s = "{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9}".format(
                        scheme["name"],
                        format_level(scheme),
                        variant["variant"],
                        scheme["type"],
                        scheme["NIST"],
                        variant["ANSSI"],
                        format_doc_code_data(variant, "sk"),
                        format_doc_code_data(variant, "pk"),
                        format_doc_code_data(variant, "ct"),
                        format_doc_code_data(variant, "ss"))
                print(s)

            if scheme["scheme"] == "Signature":
                sig = format_number(variant["sig"])
                if "sigcode" in variant:
                    sig = sig + " / " + format_number(variant["sigcode"])
                s = "{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8}".format(
                        scheme["name"],
                        format_level(scheme),
                        variant["variant"],
                        scheme["type"],
                        scheme["NIST"],
                        variant["ANSSI"],
                        format_doc_code_data(variant, "sk"),
                        format_doc_code_data(variant, "pk"),
                        format_doc_code_data(variant, "sig"))
                print(s)

filer = open("db.json")

try:
    data = json.load(filer)
    complete_tables(data)

# Semantic error in db.json.
except json.decoder.JSONDecodeError as e:
    print(str(e))
    filer.close()
    sys.exit(2)
   
# Other error.
except Exception:
    print(traceback.format_exc())
    filer.close()
    sys.exit(1)

sys.exit(0)
