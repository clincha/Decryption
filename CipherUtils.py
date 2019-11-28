ALPHABET = [chr(i) for i in range(65, 91)]  # A-Z capitals inclusive


def incrementer(string, steps):
    return ''.join(ALPHABET[(ALPHABET.index(i) + steps) % len(ALPHABET)] for i in string)
