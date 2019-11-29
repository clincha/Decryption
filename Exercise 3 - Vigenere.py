from collections import Counter

import CipherUtils

ENCRYPTED = "PTMDWEPZZLFVSIBYSQMMCYFXABGKIAEMQDLXOLPTJQPLGYXLLNPLQBZNKTRAHPGNLXNKCAXBOXYDWFGMJJXEPKMYWFOMPLXFZVRSEQTNQSIPSWSWHELDCESYFZLQSOHPYEWEPPYOHLYMZFVKDPCXYPEILOXEPZCHEPLVCYHLQQRWMHPIJWZFWTYRIDTZJDWEPEYDABWTECSRYLCOMKEPCSSIJAACMMECPPWXYLFLHAFBGQYIWGQEYATMBELBSQQESOTMQZJXSWJLLXYLYSSITJYSEKOSLPAQSMGYJBCMLNIPEWZPHOLELELBCMDCSJMCRHLBYBFPWXXMOFIPEQMYEOZACHMQSZCREOOBMELBMIZJMQSIBLZBCGBTJCPZCYXZZTMFVEPZBLVITVEHEPLJMFXQZLGPEKOVMDEIGIRTSKTBULWKPIPWCYPLRTQBMCRDLBCCQSIAOWUYWQLQPDEKOIQVIATNQSIJTOFEWBYLDZVQSMNLVPZVRSIJZUCYXELXNPRBOBMMILYMYEAETKFSIOQIRSIODACYWBZNRSIXYBGBYBYWZTPFEGMQLFDNYXMIJEYDLFRPCDXXYLFTWPPVQTXFGMLPWPEWRSIPXCBRITSQASXBDAFLHPPBSASKEPYERLMQJTXVXWQETOZVMFRZPLDZVEPPYONRDBPPXRCVCOJOZUFTWTPMIWCYZWXPEQCWJWMSPZQTRKYWNLVPZVQSSRWLAZQBTVQTHBSQQOSLCPCOIZWIPPHMCGGYKFYBMSMPLNDLMODRSDXQSMLHLBYJWSIODPYXIFEPYOFBNWKPQLCMLPGBDAYCCQSILPZBCBMSMAPBFPQE"
KEY_LENGTH = 6
ENCRYPTED_LENGTH = len(ENCRYPTED)
TESS26 = open("data/tess26.txt", "r").readline()

sameLetterSegments = [ENCRYPTED[i::6] for i in range(0, 6)]
tess26LetterFrequencies = [kvp[0] for kvp in Counter(TESS26).most_common()]

counters = [Counter(segment) for segment in sameLetterSegments]
mostCommonLettersInEachSegment = [counter.most_common()[0][0] for counter in counters]

# Currently a hack so that I can finish the rest of the exercises
mostCommonLettersInEachSegment[3] = "P"

print(mostCommonLettersInEachSegment)

steps = [ord("E") - ord(commonLetter) for commonLetter in mostCommonLettersInEachSegment]

print(steps)

decrypted = [CipherUtils.incrementer(sameLetterSegments[x], steps[x]) for x in range(len(steps))]

finalString = ""
for i in range(len(decrypted[0])):
    for j in range(len(decrypted)):
        finalString += decrypted[j][i]
print(finalString)

if finalString in TESS26:
    print("Success")
else:
    print("Failure")