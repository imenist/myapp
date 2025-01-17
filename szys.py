'''
@Coding: utf-8
@Description: 
@version: 
@Author: 陈锐填
@Date: 2020-03-29 14:59:02
@LastEditors: 陈锐填
@LastEditTime: 2020-04-11 16:29:45
@FilePath: \结对项目\szys.py
'''

import random
from fractions import Fraction
from random import randint
import numpy as np


class SZYS():
    """生成四则运算"""

    def __init__(self, total, max):
        """
        total:生成题目数量
        max:题目里数字最大数值
        """

        self.total = total
        self.max = max - 1
        self.answer = {}
        self.formula = {}
        self.formula2 = []
        # 初始化文件
        with open('docs\\Exercises.txt', 'w', encoding='utf-8') as f_n:
            f_n.write('')
        with open('docs\\Answers.txt', 'w') as f_o:
            f_o.write('')

    def store(self):
        # 调用create()，写入文件Exercise.txt,Answers.txt

        for i in range(1, self.total + 1):
            self.create_formula(i)

        with open('docs\\Answers.txt', 'a', encoding='utf-8') as f_o:
            for i in range(1, self.total + 1):
                f_o.write(str(i) + '. ' + str(self.answer[i]) + '\n')
        i = 0
        with open('docs\\Exercises.txt', 'a', encoding='utf-8') as f_n:
            for formula in self.formula.values():
                i = i + 1
                f_n.write(str(i) + '. ')
                for item in formula:
                    if type(item) is Fraction:
                        if item > 1:
                            num = item.numerator // item.denominator
                            item -= num
                            f_n.write("{}'{} ".format(num, item))
                        else:
                            f_n.write("{} ".format(item))
                    else:
                        f_n.write("{} ".format(item))
                f_n.write("=\n")

    def create_formula(self, i):
        # 生成式子
        formula = [self.create_number() if j % 2 == 1 else self.select('operation') for j in
                   range(1, self.select('operate_sum') + 1)]
        formula2 = set(formula)

        # 查重，当题目已有时重新调用create_formula()
        if self.is_equal(formula2) is True:
            self.create_formula(i)
        else:
            answer = self.get_answer(formula)
            if answer < 0:
                self.create_formula(i)
            else:
                self.answer[i] = answer
                self.formula2.append(formula2)
                self.formula[i] = formula

    def get_answer(self, formula):
        """
        给出答案
        """
        # 创建一个栈，先处理所以的 * 和 /操作

        s = []
        flag1 = 0
        for item in formula:
            if s is None:
                s.append(item)
            elif item == '*':
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
                    num = Fraction(s.pop(), item)
                    s.append(num)
                    flag1 = 0

        # 当栈里只剩一位时，即为答案
        if len(s) == 1:
            return s.pop()

        # 处理栈中的 加和减 操作，使用标志flag判断下个操作是否是减
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

    def is_equal(self, formula2):
        # 查重
        if formula2 in self.formula2:
            return True
        return False

    def create_number(self):
        """
        随机返回布尔值 , 将分数存储为列表
        True 返回整数
        False 返回分数如：五分之三表示为3/5
        """
        member = self.select('member')
        if member is True:
            return randint(1, self.max)
        else:
            fz = randint(1, self.max - 1)
            fm = randint(2, self.max)
            if fz % fm == 0:
                return self.create_number()
            else:
                return Fraction(fz, fm)

    def select(self, string):
        # 随机生成选择
        if string == 'operate_sum':
            # 返回式子的长度
            return random.choice([3, 5, 7])
        if string == 'member':
            return random.choice([True, False])
        if string == 'operation':
            return random.choice(['+', '-', '*', '÷'])
