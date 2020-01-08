import random
import os
from func.question import question
from func.file import readJsonFile


def getExam(path, clear):
    # 模拟考试（40道单选，10道多选）
    questionList = readJsonFile(path[0])
    examList = []
    while len(examList) < 40:
        flag = random.randint(0, len(questionList) - 1)
        if len(questionList[flag]['Answer']) == 1:
            examList.append(questionList[flag])
    while len(examList) < 50:
        flag = random.randint(0, len(questionList) - 1)
        if len(questionList[flag]['Answer']) > 1:
            examList.append(questionList[flag])
    count = 0
    for item in examList:
        question(item, count, len(examList), clear)
        count = count+1
    os.system(clear)
    print('考试结束，退出程序...')
