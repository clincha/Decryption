from collections import Counter

import CipherUtils

ALPHABET = [chr(i) for i in range(65, 91)]  # A-Z capitals inclusive
ALPHABET.append("|")  # Add the vertical bar to the alphabet for this exercise as we are using tess27
ENCRYPTED = "YLRTLBDYLORSVDRDJRHLLFRDYLQORZYJLZRBSJALRDYLRMVEWYRJGRDYLRSBODJKRLBWYRXQOERZBDR|JTKRJKRYLORDYOLLRELXXL|RZDJJERYLORGBWLRZQ|LTBCZRYLOROQXYDRWYLLHROLZDQKXRBXBQKZDRDYLRWJTRBK|REJJHL|RMVZQKXECRBEJKXRDYLRBKQMBEZRGEBKHRBDRDLZZRBZRZYLRBFFOJBWYL|RDYLRMBELRMQEHLOZRTQDYRYBDRSOQMZRDVOKL|R|JTKROLZDQKXRGEBDRJKRDYLQORGJOLYLB|ZRBK|RXBIQKXRJKRDYLRXOJVK|R|Q|RKJDRJSZLOALRYLORJKLRJGRDYLZLRTBZRBRZDVO|CRMQ||ELRBXL|RMBKRTYJZLREJKXRTYQDLRFQKKLORTBZRZJMLTYBDRGQKLORBK|RWELBKLORDYBKRDYLRTOBFZRJGRDYLRJDYLOZRBK|RTYJZLRPBWHLDRVK|LOKLBDYRYB|RBRFOLZLKDBSELRMBOHLDQKXRBZFLWDRDYLRMBZDLOR|BQOCMBKRJGRTYJMRZYLRTBZRQKRNVLZDRYQZR|JVSELRWYBOBWDLORBZRBRTJOHQKXRMQEHLORBK|RSVDDLORMBHLORYLOLR|VOQKXRZQUR|BCZRBK|RJKRDYLRZLALKDYRBZRBRMBKRQKRZYQKQKXRSOJB|RWEJDYRQKRYQZRGBMQECRFLTRBDRWYVOWYRSLQKXRZJRMBOHL|RBZRDJRYBALRQKZFQOL|RBROYCMLR|BQOCMBKR|QWHRBEERDYLRTLLHRJKRZVK|BCZRMQZDLOR"
TESS27 = open("data/tess27.txt").readline()

tessMostCommon = Counter(TESS27).most_common()
tessMostCommonWords = Counter(TESS27.split("|")).most_common()
encryptedMostCommon = Counter(ENCRYPTED).most_common()

# print(tessMostCommon)
# print(encryptedMostCommon)

replacements = {}
for index in range(len(ALPHABET)):
    replacements[encryptedMostCommon[index][0]] = tessMostCommon[index][0]


replacements["B"] = "A"
replacements["Y"] = "T"

replacements["D"] = "T"
replacements["Y"] = "O"

replacements["Y"] = "H"
replacements["K"] = "O"

replacements["K"] = "N"
replacements["Z"] = "O"

replacements["J"] = "O"
replacements["Z"] = "S"

replacements["G"] = "F"
replacements["V"] = "P"

replacements["O"] = "R"
replacements["Q"] = "I"

replacements["X"] = "G"
replacements["H"] = "W"

replacements["T"] = "W"
replacements["H"] = "M"

replacements["S"] = "B"
replacements["F"] = "Y"

replacements["V"] = "U"
replacements["M"] = "P"

replacements["H"] = "K"
replacements["A"] = "M"

replacements["F"] = "P"
replacements["M"] = "Y"

replacements["A"] = "V"
replacements["C"] = "M"

replacements["M"] = "M"
replacements["C"] = "Y"

replacements["I"] = "Z"
replacements["U"] = "X"

print(replacements)

decrypted = CipherUtils.replace(ENCRYPTED, replacements)

words = decrypted.split("|")
print(tessMostCommonWords)
print(Counter(words).most_common())

if "||" in decrypted:
    print("Double bars")

if decrypted in TESS27:
    print("It's been decrypted! Text is: " + decrypted)
else:
    print("Decryption failed! Text is: " + decrypted)
