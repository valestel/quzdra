import random
from morphs import *


def random_morph(morphlist):
    quantity = random.randint(0, 2)
    morph = ""
    if quantity != 0:
        k = 0
        while k < quantity:
            morph = morph+random.choice(morphlist)
            k += 1
    return morph


def generate_word(pos):
    stem = random_morph(prefixes) + random.choice(roots)
    if pos == "n" or pos == "N":
        ending = random_morph(suffixes_noun) + random.choice(flexion_noun)
    elif pos == "a" or pos == "A":
        ending = random_morph(suffixes_adj) + random.choice(flexion_adj)
    elif pos == "v" or pos == "V":
        ending = random.choice(suffixes_verb) + random.choice(flexion_verb)
    return stem + ending


def generate_list(pos, length, total):
    words = []
    while len(words) != total:
        w = generate_word(pos)
        if w not in words and len(w) <= length:
            words.append(w)
    return words


def write_list(wordlist):
    with open('fakewords.txt', 'w', encoding='utf-8') as file_out:
        for item in wordlist:
            file_out.write(item + '\n')
        file_out.close()
