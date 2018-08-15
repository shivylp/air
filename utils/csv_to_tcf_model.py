import json
import sys

def load_from_file(file):
    with open(file) as f:
        lines = f.readlines()

    final = {}
    for line in lines:
        line = line.strip()
        pre, post, strength  = line.split(",")
        if final.get(pre, None) == None:
            final[pre] = {
                "synapses": {},
            }
        strength = float(strength)
        current_value = final[pre]["synapses"].get(post, None)
        if current_value != None:
            strength += float(current_value)
        final[pre]["synapses"][post] = strength


    data = {
        "network": {
            "name": file,
            "threshold": 10,
        },
        "sensors": [],
        "actuators": [],
        "cells": final
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: " + sys.argv[0] + " <csv-file>")
    else:
        data = load_from_file(sys.argv[1])
        print(json.dumps(data))
