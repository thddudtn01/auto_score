import sys
import os

editor = "2016430018/"

execDir = "./exec/" + editor
answerDir = "./answer/"

for i in range(1,10):
    execFile = execDir + str(i) + ".out"
    if os.path.isfile(execFile):
        if os.path.isfile(answerDir + str(i) + ".txt"):
            os.remove(answerDir + str(i) + ".txt")
        for j in range(1,6):
            os.system("python forwarder.py " + str(i) + " " + str(j)
            + " | " + execFile + " >> " + answerDir + str(i) + ".txt")
