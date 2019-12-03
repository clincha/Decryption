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

_Extract from assignment brief, written by [Carlos Perez-Delgado](https://www.cs.kent.ac.uk/people/staff/cd472/)

##### Reflection
- I came into the problem trying to program too much of it straight away
- Python was a good choice
- Improving my time management skills
- Gained a good understanding of the lecture material
- I enjoyed the assignment, the challenge was interesting
- I find it difficult to communicate what code is doing

I obsessed about getting one intricate nested loop working which slowed me down during exercise 3. 
I already had the answer but I wanted to make the code do everything. This didn't work and I gave up before I could 
do it. It made me exhausted working on it and demotivated me for the next part of the assignment. 
I should have stopped when I had the correct answer and moved on. This is the same as getting an MVP done, 
you need to just get the smallest thing working before perfecting one part. Once the whole system functions, it's easy
to improve it then.

I really enjoyed working with Python, I think that it makes it a lot easier to understand what the code is doing. 
It would be interesting to do this project with a functional language like Haskell. I'd also be interested in seeing the
code that generates the assignment data. Working in a newish language when trying to do something challenging was quite
hard at times but it did make me understand Python better. 

---
### Exercise 1 (2 marks)
#### Problem
The plaintext comes from tess26.txt and is encoded with a Caesar cipher.

#### Solution
I just brute forced the text, it's quick for a computer to do for such a small range. 
The code increments each letter in the cipher text and then checks if that string is in tess26. 
If not, then increment each letter again until the string is found in the text.

##### Decrypted text
ZEDWHATWASTOBETHEINSCRIPTIONHEWASNOWHALFWAYTHROUGHTHOUSHALTNOTCOMMITHERCHEERFULFRIENDSAWHERLOOKINGSTOPPEDHISBRUSHANDSHOUTEDIFYOUWANTTOASKFOREDIFICATIONONTHESETHINGSOFMOMENTTHERESAVERYEARNESTGOODMANGOINGTOPREACHACHARITYSERMONTODAYINTHEPARISHYOUAREGOINGTOMRCLAREOFEMMINSTERIMNOTOFHISPERSUASIONNOWBUTHESAGOODMANANDHELLEXPOUNDASWELLASANYPARSONIKNOWTWASHEBEGANTHEWORKINMEBUTTESSDIDNOTANSWERSHETHROBBINGLYRESUMEDHERWALKHEREYESFIXEDONTHEGROUNDPOOHIDONTBELIEVEGODSAIDSUCHTHINGSSHEMURMUREDCONTEMPTUOUSLYWHENHERFLUSHHADDIEDAWAYAPLUMEOFSMOKESOAREDUPSUDDENLYFROMHERFATHERSCHIMNEYTHESIGHTOFWHICHMADEHERHEARTACHETHEASPECTOFTHEINTERIORWHENSHEREACHEDITMADEHERHEARTACHEMOREHERMOTHERWHOHADJUSTCOMEDOWNSTAIRSTURNEDTOGREETHERFROMTHEFIREPLACEWHERESHEWASKINDLINGBARKEDOAKTWIGSUNDERTHEBREAKFASTKETTLETHEYOUNGCHILDRENWERESTILLABOVEASWASALSOHERFATHERITBEINGSUNDAYMO

##### Key
19

---
### Exercise 2 (3 marks)
#### Problem
The plaintext comes from tess26.txt and is encoded with a Vigenere cipher using
the 21-letter key TESSOFTHEDURBERVILLES.

#### Solution
Map each letter in the key and the cipher text to their respective number.
Minus each letter value from the cipher text with each value in the key, 
looping to the end of the alphabet (26) when the value reaches the start of the alphabet (0). 

##### Decrypted text
ANUNCONSCIONABLETIMEFARLONGERT

##### Key
TESSOFTHEDURBERVILLES

---
### Exercise 3 (4 marks)
#### Problem
The plaintext comes from tess26.txt and is encoded with a Vigenere cipher. The
key is an arbitrary sequence of six letters (i.e. not necessarily forming an English word).

#### Solution
Check the letter frequency for each letter in the cipher text. Break the cipher text into 6 sections,
one for every sixth letter starting at the first to sixth letter. Perform letter frequency analysis
on each of the sections. It's likely that the key is the amount of steps from the cipher text's most
frequent letter to each sections most frequent letter. Move each section the amount of steps
that the frequent letter moved. This failed so I needed to move one letter to the second most 
frequent letter.

##### Decrypted text
ELOSSHERBABYHADNOTBEENBAPTIZEDTESSHADDRIFTEDINTOAFRAMEOFMINDWHICHACCEPTEDPASSIVELYTHECONSIDERATIONTHATIFSHESHOULDHAVETOBURNFORWHATSHEHADDONEBURNSHEMUSTANDTHEREWASANENDOFITLIKEALLVILLAGEGIRLSSHEWASWELLGROUNDEDINTHEHOLYSCRIPTURESANDHADDUTIFULLYSTUDIEDTHEHISTORIESOFAHOLAHANDAHOLIBAHANDKNEWTHEINFERENCESTOBEDRAWNTHEREFROMBUTWHENTHESAMEQUESTIONAROSEWITHREGARDTOTHEBABYITHADAVERYDIFFERENTCOLOURHERDARLINGWASABOUTTODIEANDNOSALVATIONITWASNEARLYBEDTIMEBUTSHERUSHEDDOWNSTAIRSANDASKEDIFSHEMIGHTSENDFORTHEPARSONTHEMOMENTHAPPENEDTOBEONEATWHICHHERFATHERSSENSEOFTHEANTIQUENOBILITYOFHISFAMILYWASHIGHESTANDHISSENSITIVENESSTOTHESMUDGEWHICHTESSHADSETUPONTHATNOBILITYMOSTPRONOUNCEDFORHEHADJUSTRETURNEDFROMHISWEEKLYBOOZEATROLLIVERSINNNOPARSONSHOULDCOMEINSIDEHISDOORHEDECLAREDPRYINGINTOHISAFFAIRSJUSTTHENWHENBYHERSHAMEITHADBECOMEMORENECESSARYTHANEVERTOHIDETHEMH

##### Key
PMCPIB

---
### Exercise 4 (5 marks)
#### Problem
The plaintext comes from tess26.txt and is encoded with a Vigenere cipher. The
key is an arbitrary sequence of between 4 and 6 letters.

#### Solution
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

##### Decrypted text
QUENTTOTHEIRWEDDINGDAYTHEGLOOMYINTERVENINGTIMESEEMEDTOSINKINTOCHAOSOVERWHICHTHEPRESENTANDPRIORTIMESCLOSEDASIFITNEVERHADBEENWHENEVERHESUGGESTEDTHATTHEYSHOULDLEAVETHEIRSHELTERANDGOFORWARDSTOWARDSSOUTHAMPTONORLONDONSHESHOWEDASTRANGEUNWILLINGNESSTOMOVEWHYSHOULDWEPUTANENDTOALLTHATSSWEETANDLOVELYSHEDEPRECATEDWHATMUSTCOMEWILLCOMEANDLOOKINGTHROUGHTHESHUTTERCHINKALLISTROUBLEOUTSIDETHEREINSIDEHERECONTENTHEPEEPEDOUTALSOITWASQUITETRUEWITHINWASAFFECTIONUNIONERRORFORGIVENOUTSIDEWASTHEINEXORABLEANDANDSHESAIDPRESSINGHERCHEEKAGAINSTHISIFEARTHATWHATYOUTHINKOFMENOWMAYNOTLASTIDONOTWISHTOOUTLIVEYOURPRESENTFEELINGFORMEIWOULDRATHERNOTIWOULDRATHERBEDEADANDBURIEDWHENTHETIMECOMESFORYOUTODESPISEMESOTHATITMAYNEVERBEKNOWNTOMETHATYOUDESPISEDMEICANNOTEVERDESPISEYOUIALSOHOPETHATBUTCONSIDERINGWHATMYLIFEHASBEENICANNOTSEEWHYANYMANSHOULDSOONERORLATERBEABLETOHELPDE
##### Key
GKOTK

---
### Exercise 5 (5 marks)
#### Problem
The plaintext comes from tess26.txt and is encoded with a transposition cipher,
as follows: the plaintext is written row-wise across a certain number of columns, 
between 4 and 6. (You must figure out how many columns were used.) The
ciphertext is formed by reading out successive columns from left to right.

#### Solution
I looped through each of the keys and turned the cipher text into key-length chunks. I then looped over this 2D array
column first to get some decrypted text. I checked if this text was in the document and if not I tried a higher key. 
##### Decrypted text
GHTOFGOINGAWAYFROMHIMDURINGHISABSENCEATTHEMILLBUTSHEFEAREDTHATTHISINSTEADOFBENEFITINGHIMMIGHTBETHEMEANSOFHAMPERINGANDHUMILIATINGHIMYETMOREIFITSHOULDBECOMEKNOWNMEANWHILECLAREWASMEDITATINGVERILYHISTHOUGHTHADBEENUNSUSPENDEDHEWASBECOMINGILLWITHTHINKINGEATENOUTWITHTHINKINGWITHEREDBYTHINKINGSCOURGEDOUTOFALLHISFORMERPULSATINGFLEXUOUSDOMESTICITYHEWALKEDABOUTSAYINGTOHIMSELFWHATSTOBEDONEWHATSTOBEDONEANDBYCHANCESHEOVERHEARDHIMITCAUSEDHERTOBREAKTHERESERVEABOUTTHEIRFUTUREWHICHHADHITHERTOPREVAILEDISUPPOSEYOUARENOTGOINGTOLIVEWITHMELONGAREYOUANGELSHEASKEDTHESUNKCORNERSOFHERMOUTHBETRAYINGHOWPURELYMECHANICALWERETHEMEANSBYWHICHSHERETAINEDTHATEXPRESSIONOFCHASTENEDCALMUPONHERFACEICANNOTHESAIDWITHOUTDESPISINGMYSELFANDWHATISWORSEPERHAPSDESPISINGYOUIMEANOFCOURSECANNOTLIVEWITHYOUINTHEORDINARYSENSEATPRESENTWHATEVERIFEELIDONOTDESPISEYOUANDLETMESPEAKPLAINL
##### Key
6

---
### Exercise 6 (5 marks)
#### Problem
The plaintext comes from tess26.txt and is encoded with a transposition cipher,
as follows: the plaintext is written row-wise across six columns. The ciphertext is
formed by reading out successive columns in an arbitrary order (which you must
figure out to decipher the message). Hint:look for common pairs of letters, such as
'th'.

#### Solution
This exercise was very similar to the fifth one. I broke the text into six chunks and then read each column and
tried to make a word. If this didn't work I looked for the letters TH going down and matched up as many as I could
together. I checked in tess26 and it was there. 

##### Decrypted text
RGETENDEREYESNEITHERBLACKNORBLUENORGREYNORVIOLETRATHERALLTHOSESHADESTOGETHERANDAHUNDREDOTHERSWHICHCOULDBESEENIFONELOOKEDINTOTHEIRIRISESSHADEBEHINDSHADETINTBEYONDTINTAROUNDPUPILSTHATHADNOBOTTOMANALMOSTSTANDARDWOMANBUTFORTHESLIGHTINCAUTIOUSNESSOFCHARACTERINHERITEDFROMHERRACEARESOLUTIONWHICHHADSURPRISEDHERSELFHADBROUGHTHERINTOTHEFIELDSTHISWEEKFORTHEFIRSTTIMEDURINGMANYMONTHSAFTERWEARINGANDWASTINGHERPALPITATINGHEARTWITHEVERYENGINEOFREGRETTHATLONELYINEXPERIENCECOULDDEVISECOMMONSENSEHADILLUMINATEDHERSHEFELTTHATSHEWOULDDOWELLTOBEUSEFULAGAINTOTASTEANEWSWEETINDEPENDENCEATANYPRICETHEPASTWASPASTWHATEVERITHADBEENITWASNOMOREATHANDWHATEVERITSCONSEQUENCESTIMEWOULDCLOSEOVERTHEMTHEYWOULDALLINAFEWYEARSBEASIFTHEYHADNEVERBEENANDSHEHERSELFGRASSEDDOWNANDFORGOTTENMEANWHILETHETREESWEREJUSTASGREENASBEFORETHEBIRDSSANGANDTHESUNSHONEASCLEARLYNOWASEVERTHEFAM

##### Key
234561

---
### Exercise 7 (6 marks)
#### Problem
The plaintext comes from tess27.txt and is encoded with a general substitution
cipher, using a randomly chosen mapping from the 27-character alphabet onto
itself. Note that normally (i.e. except by chance) a vertical bar will be mapped
onto some other letter of the alphabet.

#### Solution
Using frequency analysis I calculated the most likely initial substitutions. These were the punctuation bar "|" and the
letter "E". I also made the most likely substitutions for the rest of the alphabet but the bar "|" and the letter "E" would
most likely be correct, the others would need some work done to them.

I was having troubles replacing all the characters at the same time as replacing them in a for loop sometimes overrides
other values. **I found a method online that replaced all characters in one go and used that to help me**. Credit for 
this method goes to [Carl Smith](https://gist.github.com/carlsmith/b2e6ba538ca6f58689b4c18f46fef11c)

Once I had made these substitutions I knew where each word started and stopped thanks to the bar character. I split the
text into each word and found the most common words in the list. I did the same for Tess27 (the plain text file). I then
made an assumption that the most common word in the cipher text was the most common word in the plain text, "THE". I was
reassured that the letter was the because the third letter had already been converted to "E" in the first batch of replacements.

I repeated this process for the most common words until I started to understand some English words. I then made educated
guesses on what the most likely substitutions would be, using the frequency analysis' and excluding the letters I already
knew were correct. 

Finally I archived what looked correct and checked that it exists in the file Tess27. It did. 

#### Decrypted text
HE|WEATHER|BUT|TO|KEEP|THEIR|SHOES|ABOVE|THE|MULCH|OF|THE|BARTON|EACH|GIRL|SAT|DOWN|ON|HER|THREE|LEGGED|STOOL|HER|FACE|SIDEWAYS|HER|RIGHT|CHEEK|RESTING|AGAINST|THE|COW|AND|LOOKED|MUSINGLY|ALONG|THE|ANIMALS|FLANK|AT|TESS|AS|SHE|APPROACHED|THE|MALE|MILKERS|WITH|HAT|BRIMS|TURNED|DOWN|RESTING|FLAT|ON|THEIR|FOREHEADS|AND|GAZING|ON|THE|GROUND|DID|NOT|OBSERVE|HER|ONE|OF|THESE|WAS|A|STURDY|MIDDLE|AGED|MAN|WHOSE|LONG|WHITE|PINNER|WAS|SOMEWHAT|FINER|AND|CLEANER|THAN|THE|WRAPS|OF|THE|OTHERS|AND|WHOSE|JACKET|UNDERNEATH|HAD|A|PRESENTABLE|MARKETING|ASPECT|THE|MASTER|DAIRYMAN|OF|WHOM|SHE|WAS|IN|QUEST|HIS|DOUBLE|CHARACTER|AS|A|WORKING|MILKER|AND|BUTTER|MAKER|HERE|DURING|SIX|DAYS|AND|ON|THE|SEVENTH|AS|A|MAN|IN|SHINING|BROAD|CLOTH|IN|HIS|FAMILY|PEW|AT|CHURCH|BEING|SO|MARKED|AS|TO|HAVE|INSPIRED|A|RHYME|DAIRYMAN|DICK|ALL|THE|WEEK|ON|SUNDAYS|MISTER|

#### Key
######{'Cipher text value' : 'Plain text value'}
{'R': '|', 'L': 'E', 'B': 'A', 'Y': 'H', 'D': 'T', 'K': 'N', 'Z': 'S', 'O': 'R', 'J': 'O', 'Q': 'I', '|': 'D', 'E': 'L', 'M': 'M', 'X': 'G', 'T': 'W', 'W': 'C', 'V': 'U', 'H': 'K', 'S': 'B', 'G': 'F', 'F': 'P', 'C': 'Y', 'A': 'V', 'I': 'Z', 'P': 'J', 'N': 'Q', 'U': 'X'}