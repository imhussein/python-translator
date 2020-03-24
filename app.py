import json
import os
import difflib


def formatValue(value, key):
    if type(value[key]) is list:
        formatedValue = " ".join(value[key])
        return formatedValue
    else:
        return value[key]


def getWordMeaning(filename, errorMessage, wordNotExistsMessage):
    # Load Data
    data = ""
    # Check For Is Not Exists
    if os.path.exists(filename):
        data = json.load(open(filename))
    else:
        return errorMessage
    # User Input
    value = input("Enter A Word To Get Meaning ? ")
    # Transform Value
    value = value.lower()
    # Check If Word Meaning Exists
    # Return Meaning
    if value in data:
        return formatValue(data, value)
    else:
        keyValue = ""
        for key in data:
            if difflib.SequenceMatcher(None, key, value).ratio() > 0.88:
                keyValue = key
                ask = input(f"Do you mean {key} Y / N ")
                if ask is "Y":
                    return data[keyValue]
                else:
                    return wordNotExistsMessage


print(getWordMeaning("data.json",
                     "File Not Found", "Word Meaning Doesn't exists"))
