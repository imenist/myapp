'''
@Coding: utf-8
@Description: 
@version: 
@Author: 陈锐填
@Date: 2020-03-27 19:07:54
@LastEditors: 陈锐填
@LastEditTime: 2020-04-06 08:36:21
@FilePath: \结对项目\main.py
'''
"""
@Coding: utf-8
@Description:
@version:
@Author: 陈锐填
@Date: 2020-03-27 19:07:54
@LastEditors: 陈锐填
@LastEditTime: 2020-03-29 11:48:21
@FilePath: \结对项目\main.py
"""
from time import time
from szys import SZYS
import cmpAnswer
def main():
     a = SZYS(5,10)
     a.store()
    #cmpAnswer.cmp('docs\\Exercises.txt','docs\\Answers.txt','docs\\Grande.txt')
     print('yes')

if __name__ == '__main__':
    main()