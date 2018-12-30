import os

# path of your python script jackCompiler.py
pythonPath = r"D:\SCHOOL\שנה_ב\NAND\nand2tetris\projects\nand-ex1\10\project10\Main.py"

# path of folder in which there are folders.... in which there are jack files
testingPath = r"D:\SCHOOL\שנה_ב\NAND\nand2tetris\projects\nand-ex1\10\testers\p11"

def runTest(path):
    if os.path.isdir(path):
        files = os.listdir(path)
        for f in files:
            runTest(path+"/"+f)
    elif path.split(".")[-1] == "jack":
        print("running test on "+ path)
        os.system("python " + pythonPath + " " + path)
        os.system("diff -w " + path[:-4] + "xml "+ path[:-4] + "xml.cmp")

runTest(testingPath)