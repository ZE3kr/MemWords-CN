#!/usr/bin/env python3
import csv
from random import shuffle
import os

with open('word.csv', 'r') as f:
    wordList = list(csv.reader(f))

try:
    start = int(input("    Start at: "))
    end = int(input("    End at: "))
except BaseException:
    print("    Wrong index")
    exit(1)

if end - start < 5:
    print("    Wrong index")
    exit(1)

os.system('clear')

allCount = (end - start + 1) * 2
currentCount = 1

x1 = [i for i in range(start - 1, end)]
shuffle(x1)
x2 = [i for i in range(start - 1, end)]
shuffle(x2)

correct = 0
penalty = 0

for num in range(0, end - start + 1):
    print(str(currentCount) + '/' + str(allCount))
    currentCount += 1
    i = x1[num]
    print(wordList[i][1])
    userInput = input("  ")
    tried = 0
    while wordList[i][0].lower() != userInput.lower():
        if userInput == "a":
            print(wordList[i][0], i + 1)
            input("    Continue?")
            break
        else:
            hint = wordList[i][0][:tried]
            if tried < len(wordList[i][0]):
                hint += "…"
                hint += "(" + str(len(wordList[i][0]) - tried) + ")"
            print("    Wrong Answer")
            tried += 1
            print(hint)
            userInput = input("  ")
    if wordList[i][0].lower() == userInput.lower():
        print("    Accepted")
        correct += 1
        if tried != 0:
            penalty += tried
            input("    Continue?")
    os.system('clear')

    print(str(currentCount) + '/' + str(allCount))
    currentCount += 1
    i = x2[num]
    print(wordList[i][0])
    r = [i for i in range(start - 1, end)]
    r.remove(i)
    shuffle(r)
    y = [i, r[0], r[1], r[2], r[3], r[4]]
    shuffle(y)
    for index, j in enumerate(y):
        print('     ', chr(ord('A') + index) + ':', wordList[j][1])
    print('     ', 'G' + ':', 'n. 不知道')
    ans = input("    Your answer: ").lower()
    ansNum = -1
    if len(ans) == 1:
        ansNum = ord(ans) - ord('a')
    while len(ans) != 1 or ansNum >= 7 or ansNum < 0:
        ans = input("    Your answer: ").lower()
        if len(ans) == 1:
            ansNum = ord(ans) - ord('a')
    if ansNum < 6 and y[ansNum] == i:
        print("    Accepted")
        correct += 1
    else:
        print(wordList[i][1], i + 1)
        input("    Continue?")
    os.system('clear')

print("Correct: " + str(correct) + "/" + str(allCount))
print("Penalty: " + str(penalty))
