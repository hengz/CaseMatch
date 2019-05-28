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
sentences = []

preprocess = Preprocess("data/stopwords.txt")
preprocess.preprocess_text(contents, sentences)

# 使用训练集构建tfidf模型
tfidf_model = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b").fit(sentences)
sparse_data = tfidf_model.transform(sentences)

print(sparse_data)