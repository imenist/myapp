from os.path import split

import szys
import string
import getAnswer

def cmp(exerciseFile,answerFile,GrandeFile):
    correct = []
    wrong = []

    with open(exerciseFile,'r',encoding='utf-8') as f_e:
        exercice = f_e.readlines()

    with open (answerFile,'r',encoding='utf-8') as f_a:
        answerFile = f_a.readlines()

    for i in exercice:
        t = []
        exerciceNo,expression = int(i.split('.')[0]),i.split(' ')[1:-1]
        answer = answerFile[exerciceNo - 1].split('. ')[1]
        answer = answer.rsplit('\n')[0]
        for i in expression:
            if i >= '0' and i <= '9':
                i = eval(i)
            t.append(i)
        answerTrue = str(getAnswer.get_answer(t))
        if answer == answerTrue:
            correct.append(exerciceNo)
        else:
            print("错误题号:{}".format(exerciceNo))
            print("你的答案:{}".format(answer))
            print("正确答案:{}".format(answerTrue))
            wrong.append(exerciceNo)

    saveToGrande(correct,wrong,GrandeFile)

def saveToGrande(correct,wrong,GrandeFile):
    with open(GrandeFile,'w') as f_g:
        f_g.write(f'Correct:{len(correct)}{correct}\n'
                  f'Wrong:{len(wrong)}{wrong}')
