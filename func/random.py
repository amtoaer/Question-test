import random
from func.question import question
from func.file import readJsonFile
from func.error import saveError


def getRandomQuestion(path, clear):
    questionList = readJsonFile(path[0])
    while True:
        flag = random.randint(0, len(questionList) - 1)
        isWrong = question(questionList[flag], flag, len(questionList), clear)
        if isWrong:
            saveError(path[2], questionList[flag])
