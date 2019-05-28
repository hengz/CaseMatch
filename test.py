from judger import judger

def init():
    with open("data/truth.txt", "w", encoding="utf8") as f:
        for i in range(0, 500):
            f.write("B\n")

score = judger.get_score("", "data/truth.txt", "data/output.txt")
print(score)