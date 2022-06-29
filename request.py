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

filer = open("db.json")

try:
    data = json.load(filer)
    for scheme in data:
        for variant in scheme["variants"]:
            s = ""
            level = ", ".join([roman_number(i["level"]) for i in scheme["levels"]])
            pk = ""
            if "pkcode" not in variant:
                pk = format_number(variant["pk"])
            else:
                if not "pk" in variant:
                    pk = format_number(variant["pkcode"])
                else:
                    pk = format_number(variant["pk"]) + " / " + format_number(variant["pkcode"])
            if scheme["scheme"] == "KEM":
                s = "{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9}".format(
                        scheme["name"],
                        level,
                        variant["variant"],
                        scheme["type"],
                        scheme["NIST"],
                        variant["ANSSI"],
                        format_number(variant["sk"]),
                        pk,
                        format_number(variant["ct"]),
                        format_number(variant["ss"]))
                print(s)
            if scheme["scheme"] == "Signature":
                sig = format_number(variant["sig"])
                if "sigcode" in variant:
                    sig = sig + " / " + format_number(variant["sigcode"])
                s = "{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8}".format(
                        scheme["name"],
                        level,
                        variant["variant"],
                        scheme["type"],
                        scheme["NIST"],
                        variant["ANSSI"],
                        format_number(variant["sk"]),
                        pk,
                        sig)
                print(s)
                

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

filer.close()
sys.exit(0)
