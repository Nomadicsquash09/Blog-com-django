import string
from random import SystemRandom
from django.utils.text import slugify


def randon_letters(k):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=k,
    ))


def slugify_new(text, k=5):
    return slugify(text) + randon_letters(k)


# print(slugify_new('a a a a b bbabababa atenção'))
