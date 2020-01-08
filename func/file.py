import json


def readFile(path):
    fopen = open(path, 'r', encoding='UTF-8')
    content = fopen.read()
    fopen.close()
    return content


def readJsonFile(path):
    fopen = open(path, 'r', encoding='UTF-8')
    content = json.loads(fopen.read())
    fopen.close()
    return content


def saveFile(path, content):
    fopen = open(path, 'w', encoding='UTF-8')
    content = str(content)
    fopen.write(content)
    fopen.close()


def saveJsonFile(path, content):
    fopen = open(path, 'w', encoding='UTF-8')
    content = json.dumps(content, ensure_ascii=False)
    fopen.write(content)
    fopen.close()
