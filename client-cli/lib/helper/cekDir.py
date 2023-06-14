import os

def fileExist(path:str):
    if os.path.isfile(path):
        print(1)
    else:
        print(0)

def dirExist(path:str):
    if os.path.isdir(path):
        print(1)
    else:
        print(0)
