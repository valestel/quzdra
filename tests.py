import unittest
from random import choice, randint
from re import sub
from string import printable
from generate import *


class QuzdraTest(unittest.TestCase):

    chars = sub(r"[ANVanv]", "", printable)
    noun_endings = flexion_noun + [s[-1] for s in suffixes_noun] + [r[-1] for r in roots]
    sample_runs = 50

    def test_random_morph(self):
        for i in range(self.sample_runs):
            prefix = random_morph(prefixes)
            suffix_noun = random_morph(suffixes_noun)
            suffix_adj = random_morph(suffixes_adj)
            suffix_verb = random_morph(suffixes_verb)
            assert isinstance(prefix, str)
            assert isinstance(suffix_noun, str)
            assert isinstance(suffix_adj, str)
            assert isinstance(suffix_verb, str)

    def test_generate_word(self):
        for i in range(self.sample_runs):
            noun_end = generate_word(choice(("N", "n")))[-1]
            adj_end = generate_word(choice(("A", "a")))[-2:]
            verb_end = generate_word(choice(("V", "v")))[-1]
            error = generate_word(choice(self.chars))
            assert noun_end in self.noun_endings
            assert adj_end in flexion_adj
            assert verb_end in ('ь', 'я')
            assert isinstance(error, ValueError)

    def test_generate_list(self):
        nouns = generate_list('n', randint(5, 15), randint(1, 50))
        adjectives = generate_list('a', randint(5, 15), randint(1, 50))
        verbs = generate_list('v', randint(5, 15), randint(1, 50))
        errors = generate_list(choice(self.chars), randint(-100, 0), randint(-100, 0))
        for n in nouns:
            assert isinstance(n, str)
            assert n[-1] in self.noun_endings
        for a in adjectives:
            assert isinstance(a, str)
            assert a[-2:] in flexion_adj
        for v in verbs:
            assert isinstance(v, str)
            assert v[-1] in ('ь', 'я')
        assert isinstance(errors, ValueError)
