import os
import shutil
from filecmp import cmp

if os.path.isdir("./output"):
    shutil.rmtree("./output/")
else:
    print("output directoy is not existed.")

scoreD = {}
execDir = os.listdir("./exec/")
for StuID in execDir:
    os.makedirs("./output/" + StuID)
    for i in range(1,10):
        execFile = "./exec/" + StuID + "/" + str(i) + ".out"
        if os.path.isfile(execFile):
            for j in range(1,6):
                os.system("python forwarder.py " + str(i) + " " + str(j)
                + " | " + execFile + " >> ./output/" + StuID + "/"
                + str(i) + ".txt")

outputDir = os.listdir("./output/")
for StuID in outputDir:
    scoreD[StuID] = {}
    for i in range(1,10):
        answerFile = "./answer/" + str(i) + ".txt"
        if not os.path.isfile(answerFile): continue
        outputFile = "./output/" + StuID + "/" + str(i) + ".txt"
        if not os.path.isfile(outputFile):
            scoreD[StuID][i] = 0
            continue
        if cmp(answerFile, outputFile):
            scoreD[StuID][i] = 1
        else:
            scoreD[StuID][i] = 0

result = open("./result", 'w')
resultStr = ""
for StuID, StuD in scoreD.items():
    resultStr += str(StuID)
    sumScore = 0
    for number, score in StuD.items():
        resultStr += " " + str(score)
        sumScore += score
    resultStr += " " + str(sumScore)
    resultStr += "\n"

result.write(resultStr)