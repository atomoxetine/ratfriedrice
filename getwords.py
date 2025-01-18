import nltk
from nltk.corpus import brown

file = open("google-10000-english.txt", "r")
lines = file.readlines()
common_words = set()

cnt = 0
for line in lines:
    cnt += 1
    if cnt > 2000:
        break
    common_words.add(line.replace('\n', ''))

nltk.download("brown")

words = brown.tagged_words()

nouns = set()
verbs = set()

for word in words:
    name = word[0].lower()
    tag = word[1]
    if name not in common_words:
        continue
    if tag == 'NN':
        nouns.add(name)
    elif tag == 'VBN':
        verbs.add(name)

print("Nouns:")
for noun in nouns:
    print(noun)

print("Verbs:")
for verb in verbs:
    print(verb)
