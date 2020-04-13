from fractions import Fraction

def get_answer(formula):
    s = []
    s1 = []
    t = []
    flag1 = 0
    for i in formula:
        if i == "'":
            num = s.pop()
            s1.append(num)
        elif s1 and i == '/':
            flag1 = 1
        elif i == '/':
            flag1 = 2
        elif flag1 == 1:
            num1 = int(s.pop())
            num = Fraction(num1,int(i))
            num += s1.pop()
            s.append(num)
            flag1 = 0
        elif flag1 == 2:
            num = Fraction(int(s.pop()),int(i))
            s.append(num)
            flag1 = 0
        else:
            s.append(i)
    formula = s
    flag1 = 0
    s = []
    for item in formula:
        if item == '*':
            flag1 = 1
        elif item == '÷':
            flag1 = 2
        else:
            if flag1 == 0:
                s.append(item)
            if flag1 == 1:
                num = s.pop() * item
                s.append(num)
                flag1 = 0
            if flag1 == 2:
                num = Fraction(s.pop(),item)
                s.append(num)
                flag1 = 0
    if len(s) == 1:
        return s.pop()

    answer = 0
    flag = False
    for item in s:
        if item == '-':
            flag = True
        elif item != '+':
            if flag == True:
                answer -= item
            else:
                answer += item
    return answer
