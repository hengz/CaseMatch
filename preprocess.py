import re
import jieba
import pandas as pd

# 定义词性标准化函数
def preprocess_text(stopwords_path, content_lines, sentences):
    # 加载停用词
    stopwords=pd.read_csv(stopwords_path,index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')
    stopwords=stopwords['stopword'].values

    # 分词并预处理
    for line in content_lines:
        try:
            segs = list(jieba.cut(line))
            segs = [v for v in segs if not str(v).isdigit()] # drop num
            segs = [v for v in segs if not re.match('\d+(\.\d+)?', v)] # drop float num
            segs = [v.strip() for v in segs] # drop blank
            segs = [v for v in segs if len(v) > 1] # drop string with 1 charactor
            segs = [v for v in segs if v not in stopwords] # drop stop words
            sentences.append(" ".join(segs))
        except Exception:
            print(line)
            continue
            