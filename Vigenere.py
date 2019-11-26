ENCRYPTED = "TRMFQTGZGLIEBFCZBTXIXTVDGBLXYX"
KEY = "TESSOFTHEDURBERVILLES"
KEY_LENGTH = len(KEY)
LETTER_OFFSET = 65
TESS_26 = open("data/tess26.txt", "r").readline()


done = False
keyIndex = 0
decrypted = ""

for letter in ENCRYPTED:

    newLetter = ord(letter) - ord(KEY[keyIndex])

    if newLetter < 0:
        newLetter = newLetter + 26 + LETTER_OFFSET
    else:
        newLetter = newLetter + LETTER_OFFSET

    decrypted += chr(newLetter)

    if keyIndex == (KEY_LENGTH - 1):
        keyIndex = 0
    else:
        keyIndex = keyIndex + 1

if decrypted in TESS_26:
    print(decrypted)
else:
    print("failed")
