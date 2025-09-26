import random

def shuffle_word(word: str) -> str:

    # Don't shuffle if not necessary
    if len(word) <= 3:
        return word

    # Shuffle middle part
    mid = list(word[1:-1])
    random.shuffle(mid)

    # Combine string
    return word[0] + "".join(mid) + word[-1]


def shuffle_text(text: str) -> str:
    words = text.split()
    shuffled_words = [shuffle_word(word) for word in words]
    return " ".join(shuffled_words)
