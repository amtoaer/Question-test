import json
import os
from file import saveFile


def getOrderQuestion(flag1, flag2, clear, path, judge):
    fopen = open(path, 'r', encoding='UTF-8')
    questionList = json.loads(fopen.read())
    fopen.close()
    # judge用于判断是马原还是毛概
    if judge:
        flag = flag1
    else:
        flag = flag2
    while flag < len(questionList):
        i = questionList[flag]
        while True:
            os.system(clear)
            print(flag + 1, '/', len(questionList))
            if len(i['Answer']) > 1:
                print('注意:此题为多选题')
            print(i['Description'])
            for item in i['Choice']:
                print(item)
            answer = input('请输入答案:')
            if answer == i['Answer']:
                break
        flag = flag + 1
        # 判断存档顺序
        if judge:
            saveFile(flag, flag2)
        else:
            saveFile(flag1, flag)
