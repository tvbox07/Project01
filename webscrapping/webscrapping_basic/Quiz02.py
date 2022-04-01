from random import *

words = ["apple", "banana", "orange"]
word = choice(words)
# word = "apple"
print("answer : " + word)
# letters = "ap"
letters = ""


while True:
    succeed = True
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    # break
    print()

    if succeed:
        print("Success")
        break

    letter = input("Input letter > ")  #사용자 입력받기
    if letter not in letters:
        letters += letter
    if letter in word:
        print("correct")
    else:
        print("wrong")
    # if letters == word:
    #     print(letters)
    #     break
    

