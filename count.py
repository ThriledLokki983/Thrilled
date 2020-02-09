import re

n = input("Input: ")
sent = 0
words = len(re.findall('\w+', n))
for c in n:
    if c == "?" or c == "!" or c == '.':
        sent += 1
print(f"Words: {words} \n", end="")
print(f"Sentence: {sent} \n", end="")
