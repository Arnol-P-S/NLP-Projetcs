import re
import sys
F = open(<file_path>, "r")
SENT = F.read()
# counting occurance of vul,pos,neg tags
VUL_COUNT = SENT.count("S-Vul")
POS_COUNT = SENT.count("S-Pos")
NEG_COUNT = SENT.count("S-Neg")
# finding total no.of words in the file
RES = len(re.findall(r'\w+', SENT))
# loading data
T = open(<file_path>, "r")
TL = T.read()
sys.stdout = open(<file_path>, "r")
print(TL)
if (VUL_COUNT == 0 and POS_COUNT == 0 and NEG_COUNT == 0):
    print("么 Neutral  么\n")
    print("")
if VUL_COUNT >= 1:
    print("么 The video comments contain Adult content 么\n")
    print("")
if POS_COUNT > NEG_COUNT:
    if VUL_COUNT == 0:
        print("么 The video contain watchable content 么\n")
        print("")
if NEG_COUNT > POS_COUNT:
    if VUL_COUNT == 0:
        print("么 The video comments doesn't contain Adult content 么\n")
        print("")
sys.stdout.close()
