#!/usr/local/bin/python3

# Script to convert the following format into a connectome
# json format:
# {"pre-cellA": [{"post-cella": weight}, {"post-cellb": weight}....] ....}

import json

def make_connectome(file):
    with open(file) as f:
        data = json.load(f)
    cells = {}
    for src in data:
        synapses = data[src]
        cells[src]= {
            "synapses": {}
        }
        for synapse in synapses:
            postCell = tuple(synapse)[0]
            strength = float(synapse[postCell])
            if cells[src]["synapses"].get(postCell, None) != None:
                strength += cells[src]["synapses"][postCell]
            cells[src]["synapses"][postCell] = strength
    conn = {
        "network": {
            "name": "C.Elegans",
            "threshold": 30
        },
        "cells": cells
    }
    return conn


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("usage: " + sys.argv[0] + " <json-file>")
    else:
        conn = make_connectome(sys.argv[1])
        print(json.dumps(conn))
