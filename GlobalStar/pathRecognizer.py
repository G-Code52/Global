import os

def obtainPathRawlogs():
    return os.path.join(os.getcwd(), 'rawLogs')

def obtainPathConcateFiles():
    return os.path.join(os.getcwd(), 'concateFiles')

def obtainPathTxtResult(name):
    return os.path.join(os.getcwd(), 'resultTxt', name)

def obtainPathExcellResult():
    return os.path.join(os.getcwd(), 'excellResult')