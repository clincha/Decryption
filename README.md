#### CO634 Cryptography Assignment 
##### Introduction
This assessment comprises seven exercises, unimaginatively called Exercise 1 to
Exercise 7. For each exercise you will be given an extract from Thomas Hardy's
novel Tess of the d'Urbervilles (first published in 1891), encrypted with one of the
ciphers we discussed earlier in the course. Your job is to decrypt the extract, recovering
the plaintext. In each exercise, every student will be given a different extract to decipher,
and the encryption key will vary from student to student; however, all the extracts within
a particular exercise will be encoded with the same sort of cipher, as described below.
For example, in Exercise 1 everyone will have an extract encoded with a Caesar cipher.
You are free to work with colleagues in devising methods for decrypting particular sorts
of cipher, and in putting together programs to help you do so; however, when it comes
to decrypting your own individual pieces of ciphertext, you must work individually,
without help from anyone else.
Brute-force methods are not ruled out; however, you may find the assessment more
rewarding if you introduce an analytical component into your decryption tactics.

#### Exercise 1 (2 marks)
##### Problem
The plaintext comes from tess26.txt and is encoded with a Caesar cipher.

##### Solution
I decided to use the brute force technique. The code increments each letter in the cipher text 
and then checks if that string is in tess26. If not, then increment each letter again until the 
string is found in the text.

###### Decrypted text
ZEDWHATWASTOBETHEINSCRIPTIONHEWASNOWHALFWAYTHROUGHTHOUSHALTNOTCOMMITHERCHEERFULFRIENDSAWHERLOOKINGSTOPPEDHISBRUSHANDSHOUTEDIFYOUWANTTOASKFOREDIFICATIONONTHESETHINGSOFMOMENTTHERESAVERYEARNESTGOODMANGOINGTOPREACHACHARITYSERMONTODAYINTHEPARISHYOUAREGOINGTOMRCLAREOFEMMINSTERIMNOTOFHISPERSUASIONNOWBUTHESAGOODMANANDHELLEXPOUNDASWELLASANYPARSONIKNOWTWASHEBEGANTHEWORKINMEBUTTESSDIDNOTANSWERSHETHROBBINGLYRESUMEDHERWALKHEREYESFIXEDONTHEGROUNDPOOHIDONTBELIEVEGODSAIDSUCHTHINGSSHEMURMUREDCONTEMPTUOUSLYWHENHERFLUSHHADDIEDAWAYAPLUMEOFSMOKESOAREDUPSUDDENLYFROMHERFATHERSCHIMNEYTHESIGHTOFWHICHMADEHERHEARTACHETHEASPECTOFTHEINTERIORWHENSHEREACHEDITMADEHERHEARTACHEMOREHERMOTHERWHOHADJUSTCOMEDOWNSTAIRSTURNEDTOGREETHERFROMTHEFIREPLACEWHERESHEWASKINDLINGBARKEDOAKTWIGSUNDERTHEBREAKFASTKETTLETHEYOUNGCHILDRENWERESTILLABOVEASWASALSOHERFATHERITBEINGSUNDAYMO

###### Key
19

---

#### Exercise 2 (3 marks)
##### Problem
The plaintext comes from tess26.txt and is encoded with a Vigenere cipher using
the 21-letter key TESSOFTHEDURBERVILLES.

##### Solution
Map each letter in the key and the cipher text to their respective number.
Minus each letter value from the cipher text with each value in the key, 
looping to the end of the alphabet (26) when the value reaches the start of the
alphabet (0). 

###### Decrypted text
ANUNCONSCIONABLETIMEFARLONGERT

###### Key
TESSOFTHEDURBERVILLES

---

#### Exercise 3 (4 marks)
##### Problem
The plaintext comes from tess26.txt and is encoded with a Vigenere cipher. The
key is an arbitrary sequence of six letters (i.e. not necessarily forming an English
word).

##### Solution
Check the letter frequency for each letter in the cipher text. Break the cipher text into 6 sections,
one for every sixth letter starting at the first to sixth letter. Perform letter frequency analysis
on each of the sections. It's likely that the key is the amount of steps from the cipher text's most
frequent letter to each sections most frequent letter. Move each section the amount of steps
that the frequent letter moved. This failed so I needed to move one letter to the second most 
frequent letter.

###### Decrypted text
ELOSSHERBABYHADNOTBEENBAPTIZEDTESSHADDRIFTEDINTOAFRAMEOFMINDWHICHACCEPTEDPASSIVELYTHECONSIDERATIONTHATIFSHESHOULDHAVETOBURNFORWHATSHEHADDONEBURNSHEMUSTANDTHEREWASANENDOFITLIKEALLVILLAGEGIRLSSHEWASWELLGROUNDEDINTHEHOLYSCRIPTURESANDHADDUTIFULLYSTUDIEDTHEHISTORIESOFAHOLAHANDAHOLIBAHANDKNEWTHEINFERENCESTOBEDRAWNTHEREFROMBUTWHENTHESAMEQUESTIONAROSEWITHREGARDTOTHEBABYITHADAVERYDIFFERENTCOLOURHERDARLINGWASABOUTTODIEANDNOSALVATIONITWASNEARLYBEDTIMEBUTSHERUSHEDDOWNSTAIRSANDASKEDIFSHEMIGHTSENDFORTHEPARSONTHEMOMENTHAPPENEDTOBEONEATWHICHHERFATHERSSENSEOFTHEANTIQUENOBILITYOFHISFAMILYWASHIGHESTANDHISSENSITIVENESSTOTHESMUDGEWHICHTESSHADSETUPONTHATNOBILITYMOSTPRONOUNCEDFORHEHADJUSTRETURNEDFROMHISWEEKLYBOOZEATROLLIVERSINNNOPARSONSHOULDCOMEINSIDEHISDOORHEDECLAREDPRYINGINTOHISAFFAIRSJUSTTHENWHENBYHERSHAMEITHADBECOMEMORENECESSARYTHANEVERTOHIDETHEMH

###### Key
PMCPIB

---

#### Exercise 4 (5 marks)
##### Problem
The plaintext comes from tess26.txt and is encoded with a Vigenere cipher. The
key is an arbitrary sequence of between 4 and 6 letters.

##### Solution
I took the cipher text and I looked at the most frequent letters in the text: 'E', 'T', 'A', 'O', 'H', 'N'

I then broke the cipher text into four sections. 
I did this by taking every fourth letter and putting them together as follows:

Cipher text: ABCDEFGH

Sections: [A,E] [B,F] [C,G] [C,H]

I then found the most common letters in each of those segments

I found the difference between the most common letters of the cipher text and the most common letters of the segments.
I then shifted each letter in that section by that difference and then reassembled the text by putting each letter in
it's original space.

I did this process for every 4 letter, 5 letter and 6 letter key length

The five letter key seemed to work the best. I could see English letters forming but they were broken up slightly.
I tweaked the key by moving each letter to the second most common letter in that segment and looking again I repeated
that process until I had a piece from the text. 

I tried to automate the entire process by code but I struggled with checking the less frequent characters, given more 
time I would have liked to completely automate this. 

###### Decrypted text
QUENTTOTHEIRWEDDINGDAYTHEGLOOMYINTERVENINGTIMESEEMEDTOSINKINTOCHAOSOVERWHICHTHEPRESENTANDPRIORTIMESCLOSEDASIFITNEVERHADBEENWHENEVERHESUGGESTEDTHATTHEYSHOULDLEAVETHEIRSHELTERANDGOFORWARDSTOWARDSSOUTHAMPTONORLONDONSHESHOWEDASTRANGEUNWILLINGNESSTOMOVEWHYSHOULDWEPUTANENDTOALLTHATSSWEETANDLOVELYSHEDEPRECATEDWHATMUSTCOMEWILLCOMEANDLOOKINGTHROUGHTHESHUTTERCHINKALLISTROUBLEOUTSIDETHEREINSIDEHERECONTENTHEPEEPEDOUTALSOITWASQUITETRUEWITHINWASAFFECTIONUNIONERRORFORGIVENOUTSIDEWASTHEINEXORABLEANDANDSHESAIDPRESSINGHERCHEEKAGAINSTHISIFEARTHATWHATYOUTHINKOFMENOWMAYNOTLASTIDONOTWISHTOOUTLIVEYOURPRESENTFEELINGFORMEIWOULDRATHERNOTIWOULDRATHERBEDEADANDBURIEDWHENTHETIMECOMESFORYOUTODESPISEMESOTHATITMAYNEVERBEKNOWNTOMETHATYOUDESPISEDMEICANNOTEVERDESPISEYOUIALSOHOPETHATBUTCONSIDERINGWHATMYLIFEHASBEENICANNOTSEEWHYANYMANSHOULDSOONERORLATERBEABLETOHELPDE
###### Key
GKOTK

---
#### Exercise 5 (5 marks)
##### Problem
The plaintext comes from tess26.txt and is encoded with a transposition cipher,
as follows: the plaintext is written row-wise across a certain number of columns, 
between 4 and 6. (You must figure out how many columns were used.) The
ciphertext is formed by reading out successive columns from left to right.

##### Solution

###### Decrypted text

###### Key

---
##### Exercise 6 (5 marks)
##### Problem
The plaintext comes from tess26.txt and is encoded with a transposition cipher,
as follows: the plaintext is written row-wise across six columns. The ciphertext is
formed by reading out successive columns in an arbitrary order (which you must
figure out to decipher the message). Hint:look for common pairs of letters, such as
'th'.

##### Solution

###### Decrypted text

###### Key

---
##### Exercise 7 (6 marks)
##### Problem
The plaintext comes from tess27.txt and is encoded with a general substitution
cipher, using a randomly chosen mapping from the 27-character alphabet onto
itself. Note that normally (i.e. except by chance) a vertical bar will be mapped
onto some other letter of the alphabet.

##### Solution

###### Decrypted text

###### Key
