import sys
import time
"""
for i in range(1, 10):
    try:
        inputTxt.append(open("./input/" + str(i) + ".txt", 'r'))
    except IOError:
        inputTxt.append(False)
"""

idx = sys.argv[1]
trial = int(sys.argv[2])
try:
    inputTxt = open("./input/" + idx + ".txt", 'r')
except IOError:
    inputTxt = False

if inputTxt != False:
    for i in range(0,trial):
        if inputTxt == False: break
        line = inputTxt.readline().rstrip("\n")
        if not line: break

    inputData = line.split("|")
    for data in inputData:
        print(data)