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
    return i.capitalize()

# t can be a scheme (genereral) or a variant
# key is the key for which "notekey" is used
def format_notes(t, key):
    k = "notes" + key
    if k not in t:
        return ""
    s = " [[{0}](#{0})".format(t[k][0]["note"])
    for i in range(1, len(t[k])):
        s = s + ", [{0}](#{0})".format(t[k][i]["note"])
    s = s + "]"
    return s

# key can be: sk, pk, sig, ct, ss
def format_doc_code_data(variant, key):
    keycode = key + "code"
    keypossible = key + "possible"
    if key in variant and keycode in variant :
        return format_number(variant[key]) + format_notes(variant, key) + " / " + format_number(variant[keycode]) + format_notes(variant, keycode)
    elif key in variant:
        if keypossible in variant:
            return format_number(variant[key]) + format_notes(variant, key) + " (ex: " + format_number(variant[keypossible]) + format_notes(variant, keypossible) + ")"
        return format_number(variant[key]) + format_notes(variant, key)
    elif keycode in variant:
        return format_number(variant[keycode]) + format_notes(variant, keycode)

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

def format_type(scheme):
    if "ZKP" in scheme["type"]:
        return scheme["type"]
    return scheme["type"].capitalize()

def process_scheme(scheme, type_scheme):
    for variant in scheme["variants"]:
        D = {}
        for key in scheme:
            if key != "variants":
                D[key] = scheme[key]
        D["variantdetails"] = variant
        type_scheme.append(D)

def sorted_KEM_bandwidth(scheme):
    variant = scheme["variantdetails"]
    pk = 0
    pkcode = 0
    ct = 0
    ctcode = 0
    if "pk" in variant:
        pk = int(variant["pk"])
    if "pkcode" in variant:
        pkcode = int(variant["pkcode"])
    if "ct" in variant:
        ct = int(variant["ct"])
    if "ctcode" in variant:
        ctcode = int(variant["ctcode"])
    return max(pk, pkcode) + max(ct, ctcode)

def sorted_signature_bandwidth(scheme):
    variant = scheme["variantdetails"]
    pk = 0
    pkcode = 0
    sig = 0
    sigcode = 0
    if "pk" in variant:
        pk = int(variant["pk"])
    if "pkcode" in variant:
        pkcode = int(variant["pkcode"])
    if "sig" in variant:
        if variant["sig"].isdigit():
            sig = int(variant["sig"])
        else:
            sig = int(variant["sigpossible"])
    if "sigcode" in variant:
        sigcode = int(variant["sigcode"])
    return max(pk, pkcode) + max(sig, sigcode)

def sorted_NIST_status(scheme):
    if "alternate" in scheme["NIST"]:
        return 2
    elif "finalist" in scheme["NIST"]:
        return 1
    elif "standard" in scheme["NIST"]:
        return 0

def complete_tables(data):
    KEM = []
    signature = []
    for scheme in data:
        if scheme["scheme"] == "KEM":
            process_scheme(scheme, KEM)
        elif scheme["scheme"] == "Signature":
            process_scheme(scheme, signature)

    # KEM = sorted(KEM, key=sorted_KEM_bandwidth)
    # signature = sorted(signature, key=sorted_signature_bandwidth)
    KEM = sorted(KEM, key=sorted_NIST_status)
    signature = sorted(signature, key=sorted_NIST_status)

    print("")
    print("### Post-quantum cryptography key exchange mechanisms and their usage for (French) certification")
    print("")
    print("| KEM | Security Levels | Variant (levels IV / V) | Type | NIST | ANSSI [[ANSSI](#ANSSI)] | sk size (bytes) | pk size (bytes) | ct size (bytes) | ss size (bytes) |")
    print("| --- | --- | --- | --- | --- | --- | --- |  --- | --- | --- |")
    for scheme in KEM:
        variant = scheme["variantdetails"]
        s = "| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |".format(
                scheme["name"],
                format_level(scheme),
                variant["variant"] + format_variant_level(variant) + format_notes(variant, "variant"),
                scheme["type"].capitalize(),
                scheme["NIST"].capitalize() + format_notes(scheme, "NIST"),
                variant["ANSSI"].capitalize() + format_notes(variant, "ANSSI"),
                format_doc_code_data(variant, "sk"),
                format_doc_code_data(variant, "pk"),
                format_doc_code_data(variant, "ct"),
                format_doc_code_data(variant, "ss"))
        print(s)

    print("")
    print("### Post-quantum cryptography signatures and their usage for (French) certification")
    print("")
    print("| Signature | Security Levels | Variants (levels IV / V) | Type | NIST | ANSSI [[ANSSI](#ANSSI)] | sk size (bytes) |  pk size (bytes) | sig size (bytes) |")
    print("| --- | --- | --- | --- | --- | --- | --- |  --- | --- |")
    for scheme in signature:
        variant = scheme["variantdetails"]
        s = "| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |".format(
                scheme["name"],
                format_level(scheme) + format_notes(scheme, "levels"),
                variant["variant"] + format_variant_level(variant),
                format_type(scheme),
                scheme["NIST"].capitalize() + format_notes(scheme, "NIST"),
                variant["ANSSI"].capitalize() + format_notes(variant, "ANSSI"),
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
