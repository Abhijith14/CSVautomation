import pandas as pd
import shutil
from pathlib import Path

def move_contains_file(name):
    spath = "xyz/" + name
    dpath = "abc/" + name

    print("The keyword - 'v2eTechnologies' was found in " + name)

    if Path(dpath).exists():
        print(name + " file already exists in the directory abc!!!")
    else:
        shutil.move(spath, dpath)
        print("Copied "+name+" to abc !!!")

try:
    dt1 = pd.read_csv("xyz/input1.csv")
    dt2 = pd.read_csv("xyz/input2.csv")
except:
    print("Files are missing in the directory. Check xyz folder...")
    exit()

for i in dt1.columns:
    if i == "v2eTechnologies":
        move_contains_file("input1.csv")
for i in dt2.columns:
    if i == "v2eTechnologies":
        move_contains_file("input2.csv")