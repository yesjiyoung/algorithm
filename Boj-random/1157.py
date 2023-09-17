import sys
from collections import Counter

word=sys.stdin.readline().rstrip().upper()

if len(word) == 1:
    print(word)
elif len(set(word)) == 1:
    print(word[0])
else:
    c1, c2 = Counter(word).most_common(2)
    if c1[1] > c2[1]: print(c1[0])
    else: print("?")