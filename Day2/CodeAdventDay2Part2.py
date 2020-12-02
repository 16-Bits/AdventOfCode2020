# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 00:41:51 2020

@author: 16-Bit
"""
import re
def main():
    validNum = 0
    data = open('input2.txt', 'r')
    for line in data:
        intRange = re.findall('\d+', line)#gets indexs as a list of 2 numbers using regex
        charLook = re.findall('[a-z]{1}(?=:)', line)[0]#gets the character to look for using regex
        strPass = re.findall('(?!:\s)[a-z]+$', line)[0]#gets the password using regex
        if (strPass[int(intRange[0])-1]==charLook)^(strPass[int(intRange[1])-1]==charLook):#checks to see if only 1 index is correct, password is 1 indexed
              validNum +=1
    print(validNum)
if __name__ == '__main__':
    main()
