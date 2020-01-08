import os
from func.file import readJsonFile, saveJsonFile
from func.question import question


def getError(path, clear):
    questionList = readJsonFile(path[2])
    if len(questionList) == 0:
        print('错题本为空！正在退出...')
        return
    count = 0
    # 拷贝questionList的初始长度
    length = len(questionList)
    for item in questionList[:]:
        isWrong = question(item, count, length, clear)
        if isWrong == False:  # 第一次即做对判定为已经掌握
            questionList.remove(item)
            # 实时更新
            saveJsonFile(path[2], questionList)
        count = count + 1
    os.system(clear)
    print('错题本已刷完，已掌握的题目（一次答对的题目）已自动去除！\n正在退出...')


def saveError(path, item):
    # 用于添加题目到错题本
    questionList = readJsonFile(path)
    if item not in questionList:
        questionList.append(item)
    saveJsonFile(path, questionList)
