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
        intRange = re.findall('\d+', line)#returns frequency range as a list of 2 numbers using regex
        charLook = re.findall('[a-z]{1}(?=:)', line)#returns the character to look for using regex
        freq = line.count(charLook.pop())-1#finds character frequency
        if int(intRange[0]) <= freq <= int(intRange[1]):#checks if freqency is within range
              validNum += 1
    print(validNum)
if __name__ == '__main__':
    main()
