# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 02:08:33 2020

@author: 16-Bit
"""
def main():
    listTree=[]
    slopeTree=[]
    prodTree=1
    data=open('input3.txt', 'r')
    for line in data:#turn tree rows into list
        listTree.append(line)
    for i in range (1,8,2):#first 4 traverse rules: 1,3,5,7 along the row
        slopeTree.append(traverseSlope(listTree, i, 1))
    slopeTree.append(traverseSlope(listTree, 1, 2))#last traverse rule, 1 along the row, 2 down
    for elem in slopeTree:
        prodTree*=int(elem)
    print(prodTree)
def traverseSlope(slope, moveX, moveY):
    numTree=0
    xPos=0#starting position of line index
    for elem in slope[moveY::moveY]:#skip moveY rows
        xPos+=moveX#move index up by moveX
        if xPos >= (len(elem)-1):#check for index out of bound, aka loop around
            #get remainder by modulo of position by string length -1
            #-1 accounts for 1 based indexing of len() func
            xPos = xPos%(len(elem)-1)
        if elem[xPos]=='#':#check for tree at position
            numTree+=1
    return(numTree)
if __name__ == '__main__':
    main()

