import sys
from collections import defaultdict

anagrams = defaultdict(list)

# Read key-value pairs from mapper
for line in sys.stdin:
    key, word = line.strip().split('\t', 1)
    anagrams[key].append(word)

# Output groups that have at least 2 words (actual anagrams)
for key, words in anagrams.items():
    if len(words) > 1:
        print(f"{key}\t{' '.join(words)}")