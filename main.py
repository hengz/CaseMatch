import json
from preprocess import Preprocess
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

se = set()

with open("data/input.txt", "r", encoding="utf8") as f:
    for line in f:
        x = json.loads(line)
        se.add(x["A"])
        se.add(x["B"])
        se.add(x["C"])

contents = list(se)

preprocess = Preprocess("data/stopwords.txt")
sentences = preprocess.preprocess_text(contents)

# 使用训练集构建tfidf模型
tfidf_model = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b").fit(sentences)
sparse_data = tfidf_model.transform(sentences)

# print(sparse_data) 

f = open("data/input.txt", "r", encoding="utf8")
ouf = open("data/output_tfidf.txt", "w", encoding="utf8")
for line in f:
    x = json.loads(line)
    y = preprocess.preprocess_text([x["A"], x["B"], x["C"]])

    y = tfidf_model.transform(y)
    y = y.todense()

    v1 = np.sum(np.dot(y[0], np.transpose(y[1])))
    v2 = np.sum(np.dot(y[0], np.transpose(y[2])))
    if v1 > v2:
        print("B", file=ouf)
    else:
        print("C", file=ouf)

f.close()
ouf.close()