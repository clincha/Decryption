import re

ALPHABET = [chr(i) for i in range(65, 91)]  # A-Z capitals inclusive


def incrementer(string, steps):
    return ''.join(ALPHABET[(ALPHABET.index(i) + steps) % len(ALPHABET)] for i in string)


#  https://gist.github.com/carlsmith/b2e6ba538ca6f58689b4c18f46fef11c
def replace(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)
