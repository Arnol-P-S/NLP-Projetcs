import sys
import nltk
with open(<file_path>, 'r') as mfile:
    # load the data
    DATA = mfile.read()
sys.stdout = open(<file_path>, "a")
# tokenization
S = nltk.word_tokenize(DATA)
for word in S:
    print(word)
sys.stdout.close()
