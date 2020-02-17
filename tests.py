import unittest
from generate import *


class QuzdraTest(unittest.TestCase):

    chars = '1234567890-+_!@#$%^&*(){}[],./?<>:"|`~' + 'bcdefghijklmopqrstuwxyz' + 'BCDEFGHIJKLMOPQRSTUWXYZ' + \
            'АБВГДЕËЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
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
            noun = generate_word(random.choice(("N", "n")))
            adj = generate_word(random.choice(("A", "a")))
            verb = generate_word(random.choice(("V", "v")))
            error = generate_word(random.choice(self.chars))
            assert noun[-1] in flexion_noun or noun[-1] in [s[-1] for s in suffixes_noun] + [r[-1] for r in roots]
            assert adj[-2:] in flexion_adj
            assert verb[-1] in ('ь', 'я')
            assert isinstance(error, ValueError)

    def test_generate_list(self):
        nouns = generate_list('n', random.randint(5, 15), random.randint(1, 50))
        adjectives = generate_list('a', random.randint(5, 15), random.randint(1, 50))
        verbs = generate_list('v', random.randint(5, 15), random.randint(1, 50))
        errors = generate_list(random.choice(self.chars), random.randint(-100, 0), random.randint(-100, 0))
        for n in nouns:
            assert isinstance(n, str)
            assert n[-1] in flexion_noun or n[-1] in [s[-1] for s in suffixes_noun] + [r[-1] for r in roots]
        for a in adjectives:
            assert isinstance(a, str)
            assert a[-2:] in flexion_adj
        for v in verbs:
            assert isinstance(v, str)
            assert v[-1] in ('ь', 'я')
        assert isinstance(errors, ValueError)
