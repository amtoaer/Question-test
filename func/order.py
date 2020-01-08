import json
import os
from func.file import *
from func.question import question


def getOrderQuestion(path, clear):
    # 参数为路径和清屏命令
    fopen = open(path[0], 'r', encoding='UTF-8')
    questionList = json.loads(fopen.read())
    fopen.close()
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
