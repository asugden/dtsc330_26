import fasttext as ft
import numpy as np
import spacy


class NounParser:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.ft_model = ft.load_model("data/cc.en.50.bin")
        self.ds = self.ft_model.get_sentence_vector("data science")

    def phrases(self, txt: str) -> list[str]:
        """Convert text into noun phrases"""
        doc = self.nlp(txt.lower())
        words = []
        for phrase in doc.noun_chunks:
            word = phrase.text
            word = word.strip()
            if not (word == "" or word.isspace()):
                words.append(word.replace("\n", ""))
        return self.clean(words)

    def clean(self, words: list[str]):
        """Remove unnecessary words"""
        out = []
        for word in words:
            if word[0] == "#":
                pass
            elif word[0] == "-" and len(word) > 2:
                out.append(word[2:])
            elif "data" in word:
                pass
            else:
                out.append(word)
        return out

    def top_n(self, words: list[str], n: int = 100):
        """Return the top N words most similar to 'data science'"""
        out = []
        for word in words:
            vec = self.ft_model.get_sentence_vector(word)
            out.append((np.abs(np.linalg.norm(vec - self.ds)), word))

        out.sort()
        return [v[1] for v in out[:n]]


def key_points(txt: str):
    nparse = NounParser()
    out = []
    for line in txt.split("\n"):
        phrases = nparse.phrases(line)
        if phrases is not None:
            out.extend(phrases)
    return nparse.top_n(list(set(out)))


if __name__ == "__main__":
    with open("SYLLABUS.md", "r") as fp:
        txt = fp.read()
        start = txt.find("# Schedule")
        txt = txt[start + 10 :]

    points = key_points(txt)
    print(points)
