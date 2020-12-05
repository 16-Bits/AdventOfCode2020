# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:19:10 2020

@author: 16-Bit
"""
import re
def main():
#    data=(open('example2.txt', 'r').read()).split('\n\n')#example input for debugging
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
        self.hgt = hgt#height
        self.hcl = hcl#hair color
        self.ecl = ecl#eye color
        self.pid = pid#passport ID
        self.cid = cid#country ID
    def __iter__(self):#iter overide to iterate over passport values, ignoring CID
        return(iter([self.byr, self.iyr, self.eyr, self.hgt, self.hcl,
                     self.ecl, self.pid]))
    def checkIfLegit(self):
        test = [self.byr, self.iyr, self.eyr, self.hgt, self.hcl,
                     self.ecl, self.pid]
        legitECL= ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']#list of real eye colors
        for value in iter(self):#checks if passport has non-empty fields
            if not value:
                return(False)
        #check if birth year is 4 digits, at least 1920, at most 2002
        if not (re.match('^[0-9]{4}$', self.byr) and 1920 <= int(self.byr) <= 2002):
            return(False)
        #check if issue year is 4 digits, at least 2010, at most 2020
        if not (re.match('^[0-9]{4}$', self.iyr) and 2010 <= int(self.iyr) <= 2020):
            return(False)
        #check if expire year is 4 digits, at least 2020, at most 2030
        if not (re.match('^[0-9]{4}$', self.eyr) and 2020 <= int(self.eyr) <= 2030):
            return(False)
        #check if height is a number followed by "cm" or "in"
        if re.match('([0-9]+)(in|cm)', self.hgt):
            #check if height in cm is at least 150, at most 193
            if re.match('[0-9]+cm', self.hgt):
                if not (150 <= int(self.hgt[:-2]) <= 193):
                    return(False)
            #check if height in in is at least 59, at most 76
            if re.match('[0-9]+in', self.hgt):
                if not (59 <= int(self.hgt[:-2]) <= 76):
                    return(False)
        else:
            return(False)
        #check if hair color is hex string
        if not (re.match('^#[a-f0-9]{6}$', self.hcl)):
            return(False)
        #checks if eye color is real
        if self.ecl not in legitECL:
            return(False)
        #check if passport ID is nine digits, including leading zeros
        if not re.match('^[0-9]{9}$', self.pid):
            return(False)
        return(True)
if __name__ == '__main__':
    main()

