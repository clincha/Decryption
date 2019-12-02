from collections import Counter

import CipherUtils

ALPHABET = [chr(i) for i in range(65, 91)]  # A-Z capitals inclusive
ALPHABET.append("|")  # Add the vertical bar to the alphabet for this exercise as we are using tess27
ENCRYPTED = "YLRTLBDYLORSVDRDJRHLLFRDYLQORZYJLZRBSJALRDYLRMVEWYRJGRDYLRSBODJKRLBWYRXQOERZBDR|JTKRJKRYLORDYOLLRELXXL|RZDJJERYLORGBWLRZQ|LTBCZRYLOROQXYDRWYLLHROLZDQKXRBXBQKZDRDYLRWJTRBK|REJJHL|RMVZQKXECRBEJKXRDYLRBKQMBEZRGEBKHRBDRDLZZRBZRZYLRBFFOJBWYL|RDYLRMBELRMQEHLOZRTQDYRYBDRSOQMZRDVOKL|R|JTKROLZDQKXRGEBDRJKRDYLQORGJOLYLB|ZRBK|RXBIQKXRJKRDYLRXOJVK|R|Q|RKJDRJSZLOALRYLORJKLRJGRDYLZLRTBZRBRZDVO|CRMQ||ELRBXL|RMBKRTYJZLREJKXRTYQDLRFQKKLORTBZRZJMLTYBDRGQKLORBK|RWELBKLORDYBKRDYLRTOBFZRJGRDYLRJDYLOZRBK|RTYJZLRPBWHLDRVK|LOKLBDYRYB|RBRFOLZLKDBSELRMBOHLDQKXRBZFLWDRDYLRMBZDLOR|BQOCMBKRJGRTYJMRZYLRTBZRQKRNVLZDRYQZR|JVSELRWYBOBWDLORBZRBRTJOHQKXRMQEHLORBK|RSVDDLORMBHLORYLOLR|VOQKXRZQUR|BCZRBK|RJKRDYLRZLALKDYRBZRBRMBKRQKRZYQKQKXRSOJB|RWEJDYRQKRYQZRGBMQECRFLTRBDRWYVOWYRSLQKXRZJRMBOHL|RBZRDJRYBALRQKZFQOL|RBROYCMLR|BQOCMBKR|QWHRBEERDYLRTLLHRJKRZVK|BCZRMQZDLOR"
TESS27 = open("data/tess27.txt").readline()

tessMostCommon = Counter(TESS27).most_common()
encryptedMostCommon = Counter(ENCRYPTED).most_common()

print(tessMostCommon)
print(encryptedMostCommon)

replacements = {}
for index in range(len(ALPHABET)):
    replacements[encryptedMostCommon[index][0]] = tessMostCommon[index][0]

replacements["D"] = "T"
replacements["Y"] = "H"
replacements["L"] = "E"

print(replacements)

decrypted = CipherUtils.replace(ENCRYPTED, replacements)

words = decrypted.split("|")
words = [word if len(word) < 4 else None for word in words]
print(Counter(words).most_common())

if "||" in  decrypted:
    print("Double bars")

if decrypted in TESS27:
    print("It's been decrypted! Text is: " + decrypted)
else:
    print("Decryption failed! Text is: " + decrypted)
