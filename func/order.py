import os
from func.file import readFile, readJsonFile, saveFile
from func.question import question


def getOrderQuestion(path, clear):
    questionList = readJsonFile(path[0])
    # flag为当前做题进度
    flag = int(readFile(path[1]))
    while flag < len(questionList):
        i = questionList[flag]
        question(i, flag, len(questionList), clear)
        flag = flag + 1
        saveFile(path[1], flag)
    empty = input('当前题库已刷完，是否清空进度以便二刷？(y/n)\n')
    if empty == 'y':
        flag = 0
        saveFile(path[1], flag)
