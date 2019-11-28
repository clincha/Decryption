ENCRYPTED = [ord(i) for i in "TRMFQTGZGLIEBFCZBTXIXTVDGBLXYX"]
KEY = [ord(i) for i in "TESSOFTHEDURBERVILLES"]
KEY_LENGTH = len(KEY)
LETTER_OFFSET = 65
TESS26 = open("data/tess26.txt", "r").readline()

decrypted = "".join([
    chr(ENCRYPTED[index] - KEY[index % KEY_LENGTH] + LETTER_OFFSET + 26)
    if ENCRYPTED[index] - KEY[index % KEY_LENGTH] < 0 else
    chr(ENCRYPTED[index] - KEY[index % KEY_LENGTH] + LETTER_OFFSET)
    for index in range(len(ENCRYPTED))
])

if decrypted in TESS26:
    print("It's been decrypted! Text is: " + decrypted)
else:
    print("Decryption failed!  Text is: " + decrypted)
