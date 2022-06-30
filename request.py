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

# t can be a scheme (genereral) or a variant
# key is the key for which "notekey" is used
def format_notes(t, key):
    k = "notes" + key
    if k not in t:
        return ""
    s = " [[{0}](#{0})".format(t[k][0]["note"])
    for i in range(1, len(t[k])):
        s = s + ", [[{0}](#{0})".format(t[k][i]["note"])
    s = s + "]"
    return s

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

def format_variant_level(variant):
    if len(variant["levels"]) == 1:
        if variant["levels"][0]["level"] == "5":
            return ""
        elif variant["levels"][0]["level"] == "< 1":
            return ""
        else:
            return " (level {0})".format(roman_number(variant["levels"][0]["level"]))
    else:
        return " (level " + " / ".join([roman_number(i["level"]) for i in variant["levels"]]) + ")"

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
    KEM = []
    signature = []
    for scheme in data:
        if scheme["scheme"] == "KEM":
            KEM.append(scheme)
        elif scheme["scheme"] == "Signature":
            signature.append(scheme)

    print("KEM | Security Levels | Variant (best security levels) | Type | | NIST [[NIST](#NIST)] | ANSSI [[ANSSI](#ANSSI)] | sk size (bytes) | pk size (bytes) | ct size (bytes) | ss size (bytes) |")
    print("| --- | --- | --- | --- | --- | --- | --- |  --- | --- |")
    for scheme in KEM:
        for variant in scheme["variants"]:
            format_variant_level(variant)
            s = "| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |".format(
                    scheme["name"],
                    format_level(scheme),
                    variant["variant"] + format_variant_level(variant) + format_notes(variant, "variant"),
                    scheme["type"],
                    scheme["NIST"],
                    variant["ANSSI"] + format_notes(variant, "ANSSI"),
                    format_doc_code_data(variant, "sk"),
                    format_doc_code_data(variant, "pk"),
                    format_doc_code_data(variant, "ct"),
                    format_doc_code_data(variant, "ss"))
            print(s)

    print("| Signature | Security Levels | Variants (best security levels) | Type | NIST [[NIST](#NIST)] | ANSSI [[ANSSI](#ANSSI)] | sk size (bytes) |  pk size (bytes) | sig size (bytes) |")
    print("| --- | --- | --- | --- | --- | --- | --- |  --- | --- |")
    for scheme in signature:
        for variant in scheme["variants"]:
            s = "| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |".format(
                    scheme["name"],
                    format_level(scheme) + format_notes(scheme, "levels"),
                    variant["variant"] + format_variant_level(variant),
                    scheme["type"],
                    scheme["NIST"] + format_notes(scheme, "NIST"),
                    variant["ANSSI"] + format_notes(variant, "ANSSI"),
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
