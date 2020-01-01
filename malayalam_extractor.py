import re
import sys
with open(<file_path>, 'r') as mfile:
    DATA1 = mfile.read()
with open(<file_path>, 'r') as mfile:
    DATA = mfile.readlines()
sys.stdout = open(<file_path>, "a")
S1 = re.findall(u"[\u0D00-\u0D7F .]+", DATA1)
# extraction of malayalam words
for word in S1:
    print(word)
for line in DATA:
    da = eval(line)["text"]
    s = re.findall(u"[\u0D00-\u0D7F .]+", da)
    if len(s) == 0:
     	continue
    else:
    	for word in s:
        print(word)
sys.stdout.close()
