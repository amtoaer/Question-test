import json
import os
import random
from func.question import question
from func.file import readJsonFile


def getRandomQuestion(path, clear):
    questionList = readJsonFile(path[0])
    while True:
        flag = random.randint(0, len(questionList) - 1)
        question(questionList[flag], flag, len(questionList), clear)
