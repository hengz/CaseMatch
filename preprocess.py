import re
import jieba
import pandas as pd


class Preprocess:

    stopwords = []

    def __init__(self, stopwords_path):
        self.stopwords = pd.read_csv(stopwords_path, index_col=False, quoting=3, sep="\t", names=[
                                     'stopword'], encoding='utf-8')
        self.stopwords = self.stopwords['stopword'].values

    # 定义词性标准化函数
    def preprocess_text(self, content_lines, sentences):
        # 分词并预处理
        for line in content_lines:
            try:
                segs = list(jieba.cut(line))
                segs = [v for v in segs if not str(v).isdigit()]  # drop num
                segs = [v for v in segs if not re.match(
                    '\d+(\.\d+)?', v)]  # drop float num
                segs = [v.strip() for v in segs]  # drop blank
                # drop string with 1 charactor
                segs = [v for v in segs if len(v) > 1]
                # drop stop words
                segs = [v for v in segs if v not in self.stopwords]
                sentences.append(" ".join(segs))
            except Exception:
                print(line)
                continue
