import os

def fileExist(path:str):
    if os.path.isfile(path):
        return 1
    else:
        return 0

def dirExist(path:str):
    if os.path.isdir(path):
        return 1
    else:
        return 0
