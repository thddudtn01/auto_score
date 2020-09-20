import os
import shutil

sourcePath = "./source/"
if os.path.isdir("./tmp"):
    shutil.rmtree("./tmp/")
os.makedirs("./tmp")
if os.path.isfile("./copyresult.txt"):
    os.system("rm copyresult.txt")

stuDirs = os.listdir("./source/")
for stuDir in stuDirs:
    stuPath = sourcePath + str(stuDir)
    for i in range(1,6):
        codeFile = stuPath + 2*("/" + str(i)) + ".c"
        targetFile = "./tmp/" + str(stuDir) + "_" + str(i) + ".c"
        try:
            shutil.copy(codeFile, targetFile)
        except:
            print(str(stuDir) + " did not follow the rules.")
            break

for i in range(1,6):
    os.system("perl moss.pl -l c ./tmp/*_" + str(i) +".c | grep http >> copyresult.txt")