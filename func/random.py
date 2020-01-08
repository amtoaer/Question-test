import json
import os
import random
from func.question import question


def getRandomQuestion(path, clear):
    fopen = open(path[0], 'r', encoding='UTF-8')
    questionList = json.loads(fopen.read())
    fopen.close()
    while True:
        flag = random.randint(0, len(questionList) - 1)
        question(questionList[flag], flag, len(questionList), clear)
