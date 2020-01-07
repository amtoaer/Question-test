def readFile():
    fopen = open('./archive/flag', 'r', encoding='UTF-8')
    flag1 = fopen.readline()
    flag2 = fopen.readline()
    fopen.close()
    return int(flag1), int(flag2)


def saveFile(flag1, flag2):
    fopen = open('./archive/flag', 'w', encoding='UTF-8')
    flag1 = str(flag1)
    flag2 = str(flag2)
    fopen.write(flag1 + '\n' + flag2)
    fopen.close()
