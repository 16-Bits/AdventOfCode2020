# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:35:23 2020

@author: 16-Bit
"""
def main():
    listTree=[]
    numTree=0
    xPos=0#starting position of line index
    data=open('input3.txt', 'r')
    debugOut=open('debug3.1.txt', 'w+')#debug output to track position
    for line in data:#turn tree rows into list
        listTree.append(line)
    debugOut.write(listTree[0])#print skipped row in debug text
    for elem in listTree[1:]:#skip first row
        xPos+=3#move index up by 3
        if xPos >= (len(elem)-1):#check for index out of bound, aka loop around
            #get remainder by modulo of position by string length -1
            #-1 accounts for 1 based indexing of len() func
            xPos = xPos%(len(elem)-1)
        listRow=[]#converts row to list for debug output
        listRow[:0]=elem
        if elem[xPos]=='#':#check for tree at position
            numTree+=1
            listRow[xPos]='X'#debug output for tree at pos
        else:
            listRow[xPos]='O'#debug output for space at pos
        listPosData=[xPos, elem[xPos]]#debug output for current position
        debugOut.write(''.join(listRow[:len(elem)-1])+str(listPosData)+'\n')#write to debug text file
    print(numTree)
    debugOut.close()
if __name__ == '__main__':
    main()
