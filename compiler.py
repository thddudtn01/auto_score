import os
import shutil
import glob

option = " -lm"

if os.path.isdir("./exec"):
    shutil.rmtree("./exec/")
else:
    print("exec directoy is not existed.")

if os.path.isdir("./output"):
    shutil.rmtree("./output/")
else:
    print("output directoy is not existed.")

root = os.listdir("./source/")

for StuID in root:
    os.makedirs("./exec/" + StuID)
    os.makedirs("./output/" + StuID)
    StuDir = os.listdir("./source/" + StuID)

    for codeDir in StuDir:
        DestFile = "./exec/" + StuID + "/" + codeDir + ".out "
        TargetFile = "./source/" + StuID + ("/" + codeDir)*2 + ".c"
        files = glob.glob("./source/" + StuID + "/" + codeDir + "/*.c")
        TargetFiles = ""
        for i in range(0, len(files)):
            TargetFiles = TargetFiles + " " + files[i]

        if os.path.isfile(TargetFile):
            os.system("gcc -o " + DestFile + TargetFiles + option)
      