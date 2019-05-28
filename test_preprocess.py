from preprocess import Preprocess

sentences = []
content_lines = ["这是测试的第一句话121记者", "这是测试的第二句话121记者", "这是测试的第三句话121记者"]

preprocess = Preprocess("data/stopwords.txt")
preprocess.preprocess_text(content_lines, sentences)

print(sentences)