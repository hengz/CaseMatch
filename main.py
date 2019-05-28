import json
import preprocess 

A = []
B = []
C = []

with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        x = json.loads(line)
        A.add(x["A"])
        B.add(x["B"])
        C.add(x["C"])



