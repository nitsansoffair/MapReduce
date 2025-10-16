import sys

# Each line is a word
for line in sys.stdin:
    word = line.strip()
    if word:
        # Sort letters alphabetically; e.g., "listen" -> "eilnst"
        key = ''.join(sorted(word))
        # Output: key \t word
        print(f"{key}\t{word}")