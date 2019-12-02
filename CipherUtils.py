import re

ALPHABET = [chr(i) for i in range(65, 91)]  # A-Z capitals inclusive


def incrementer(string, steps):
    return ''.join(ALPHABET[(ALPHABET.index(i) + steps) % len(ALPHABET)] for i in string)


#  carlsmith/replace.py
def replace(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)
