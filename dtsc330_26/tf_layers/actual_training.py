import random

# from nltk.corpus import words as nltk_words
import wordfreq

from dtsc330_26.tf_layers import seq2seq_transformer

all_letters = list("abcdefghijklmnopqrstuvwxyz")
letter_neighbors = {
    "a": list("qwsxz"),
    "b": list("vfghn"),
    "c": list("xsdfv"),
    "d": list("ersfcx"),
    "e": list("wsdr"),
    "f": list("rtgvcd"),
    "g": list("tyhbvf"),
    "h": list("yunjbg"),
    "i": list("uojk"),
    "j": list("uiknhm"),
    "k": list("ioljnm"),
    "l": list("opk"),
    "m": list("njk"),
    "n": list("bhjm"),
    "o": list("ipkl"),
    "p": list("ol"),
    "q": list("wa"),
    "r": list("edft"),
    "s": list("wedxza"),
    "t": list("rfgy"),
    "u": list("yhji"),
    "v": list("cfgb"),
    "w": list("qase"),
    "x": list("zsdc"),
    "y": list("tghu"),
    "z": list("asx"),
}


def add_letter(word: str) -> str:
    letter = random.choice(all_letters)
    pos = random.randint(0, len(word))
    return word[:pos] + letter + word[pos:]


def replace_letter(word: str) -> str:
    pos = random.randint(0, len(word) - 1)
    existing = word[pos]
    if random.random() < 0.1:
        letter = random.choice(all_letters)
    else:
        letter = random.choice(letter_neighbors[existing])
    return word[:pos] + letter + word[pos + 1 :]


def remove_letter(word: str) -> str:
    pos = random.randint(0, len(word) - 1)
    return word[:pos] + word[pos + 1 :]


def switch_letters(word: str) -> str:
    pos = random.randint(0, len(word) - 2)
    return word[:pos] + word[pos + 1] + word[pos] + word[pos + 2 :]


def no_of_errs(word_len: int) -> int:
    num_errors = 1
    if word_len < 6:
        pass
    elif word_len < 9:
        num_errors = random.choices([1, 2], weights=[4, 1])[0]
    elif word_len < 12:
        num_errors = random.choices([1, 2, 3], weights=[8, 3, 1])[0]
    else:
        num_errors = random.choices([1, 2, 3, 4], weights=[8, 4, 2, 1])[0]
    return num_errors


def add_random_errors(word: str, n: int = 4) -> list[tuple[str, str]]:
    out = []

    for _ in range(n):
        num_errors = no_of_errs(len(word))
        misspelled = word
        for _ in range(num_errors):
            which_err = random.randint(0, 3)
            if which_err == 0:
                misspelled = add_letter(misspelled)
            elif which_err == 1:
                misspelled = replace_letter(misspelled)
            elif which_err == 2:
                misspelled = remove_letter(misspelled)
            else:
                misspelled = switch_letters(misspelled)
        out.append((misspelled, word))
    return out


def create_training_set():
    word_list = [
        word
        # for word in nltk_words.words()
        for word in wordfreq.top_n_list("en", 10_000)
        if len(word) > 3 and word.isascii() and word.isalpha()
    ]
    pairs = []

    for word in word_list:
        pairs.extend(add_random_errors(word.lower()))
    return pairs


if __name__ == "__main__":
    # Example trainingdata
    # pairs = [
    #     ("recieve", "receive"),
    #     ("definately", "definitely"),
    #     ("wierd", "weird"),
    #     ("adres", "address"),
    #     ("acommodate", "accommodate"),
    #     ("seperate", "separate"),
    #     ("untill", "until"),
    #     ("goverment", "government"),
    # ]
    pairs = create_training_set()

    s2s = seq2seq_transformer.Seq2SeqTransformer()
    s2s.fit(pairs)
    s2s.save("data/s2s_spelling")

    print(s2s.correct("worng"))
    print(1)
