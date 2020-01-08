import os


def question(i, flag, length, clear):
    # 该bool值用于判断是否一次做对
    isWrong = False
    while True:
        os.system(clear)
        print(flag + 1, '/', length)
        if len(i['Answer']) > 1:
            print('注意:此题为多选题')
        print(i['Description'])
        for item in i['Choice']:
            print(item)
        answer = input('请输入答案:')
        if answer == i['Answer']:
            return isWrong
        isWrong = True
