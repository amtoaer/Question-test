import os
from func.file import readFile, readJsonFile, saveFile
from func.question import question
from func.error import saveError


def getOrderQuestion(path, clear):
    questionList = readJsonFile(path[0])
    # flag为当前做题进度
    flag = int(readFile(path[1]))
    while flag < len(questionList):
        i = questionList[flag]
        isWrong = question(i, flag, len(questionList), clear)
        if isWrong:
            saveError(path[2], i)
        flag = flag + 1
        saveFile(path[1], flag)
    os.system(clear)
    empty = input('当前题库已刷完，是否清空进度以便二刷？(y/n)\n')
    if empty == 'y':
        flag = 0
        saveFile(path[1], flag)
