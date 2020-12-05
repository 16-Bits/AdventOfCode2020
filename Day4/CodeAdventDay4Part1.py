# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:19:10 2020

@author: 16-Bit
"""
import re
def main():
#    data=(open('example.txt', 'r').read()).split('\n\n')#example input for debugging
    data=(open('input4.txt', 'r').read()).split('\n\n')#read input as chunk, then split
    numValid=0#number of valid passports
    intakeBuffer={}#buffer dictionary for passport processing
    manifest=[]#list of all processed passports
    for elem in data:#process input
        strTokens=re.findall('[a-z]{3}:\S*', elem)#tokenize key:value pairs
        for elem in strTokens:#add key:value pairs to dictionary
            intakeBuffer[elem[:3]]=elem[4:]
        #add passport to manifest list
        manifest.append(Passport(intakeBuffer.get('byr'), intakeBuffer.get('iyr'),
                                    intakeBuffer.get('eyr'), intakeBuffer.get('hgt'),
                                    intakeBuffer.get('hcl'), intakeBuffer.get('ecl'),
                                    intakeBuffer.get('pid'), intakeBuffer.get('cid')))
        intakeBuffer.clear()#clear dictionary
    for object in manifest:#go through passport manifest, check if they are legit
        if object.checkIfLegit():
            numValid += 1
    print(numValid)
class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid):
        self.byr = byr#birth year
        self.iyr = iyr#issue year
        self.eyr = eyr#expire year
        self.hgt = hgt#heigt
        self.hcl = hcl#hair color
        self.ecl = ecl#eye color
        self.pid = pid#passport ID
        self.cid = cid#country ID
    def __iter__(self):#iter overide to iterate over passport values, ignoring CID
        return(iter([self.byr, self.iyr, self.eyr, self.hgt, self.hcl,
                     self.ecl, self.pid]))
    def checkIfLegit(self):#checks if passport has non-empty fields
        for value in iter(self):
            if not value:
                return(False)
        return(True)
if __name__ == '__main__':
    main()

