import json
import preprocess 

se = set()

with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        x = json.loads(line)
        se.add(x["A"])
        se.add(x["B"])
        se.add(x["C"])



