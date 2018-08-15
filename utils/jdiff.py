import jsondiff
import json
import sys


def main(f1, f2):
    with open(f1) as f:
        data1 = json.load(f)

    with open(f2) as f:
        data2 = json.load(f)

    diff = jsondiff.diff(data1, data2)
    print(diff)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: " + sys.argv[0] + " <json-file-1> <json-file-2>")
    else:
        f1 = sys.argv[1]
        f2 = sys.argv[2]
        main(f1, f2)

