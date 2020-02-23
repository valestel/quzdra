import random
from morphs import *


def random_morph(morphlist):
    quantity = random.randint(0, 2)
    morph = ""
    if quantity:
        for i in range(quantity):
            morph = morph + random.choice(morphlist)
    return morph


def generate_word(pos):
    stem = random_morph(prefixes) + random.choice(roots)
    if pos in ("n", "N"):
        ending = random_morph(suffixes_noun) + random.choice(flexion_noun)
    elif pos in ("a", "A"):
        ending = random_morph(suffixes_adj) + random.choice(flexion_adj)
    elif pos in ("v", "V"):
        ending = random.choice(suffixes_verb) + random.choice(flexion_verb)
    else:
        return ValueError("Part of speech not recognised")
    return stem + ending


def generate_list(pos, length, total):
    words = set()
    if not length or not total:
        return ValueError("Positive values should be used")
    else:
        while len(words) != total:
            w = generate_word(pos)
            if len(w) <= length:
                words.add(w)
    return words


def write_list(wordlist, result='fakewords.txt'):
    with open(result, 'w', encoding='utf-8') as file_out:
        for item in wordlist:
            file_out.write(item + '\n')
