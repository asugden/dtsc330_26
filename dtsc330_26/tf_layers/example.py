from dtsc330_26.tf_layers import seq2seq_transformer

if __name__ == "__main__":
    # Example trainingdata
    pairs = [
        ("recieve", "receive"),
        ("definately", "definitely"),
        ("wierd", "weird"),
        ("adres", "address"),
        ("acommodate", "accommodate"),
        ("seperate", "separate"),
        ("untill", "until"),
        ("goverment", "government"),
    ]

    s2s = seq2seq_transformer.Seq2SeqTransformer()
    s2s.fit(pairs)

    print(s2s.correct("worng"))
    print(1)
