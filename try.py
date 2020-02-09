import re

sent = -1
n = input("Text: ")
sent = len(re.split(r'[\.!?]+', n))
print(f"{sent}", end="")

