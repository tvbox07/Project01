from random import *

words = ["apple", "banana", "orange"]
word = choice(words)
print("answer : " + word)
letters = "ap"


while True:
    for w in word:
        if w in letters:
            print(w, end="")
        else:
            print("_", end="")

    break