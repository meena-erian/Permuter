#Copyright (c) 2016 Meena Erian Awad Hanna
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#Note: This program was originally created in C++ and translated literally; This Python version may require some improvements


def Factorial(n):
    Answer=1
    while n>1:
        Answer*=n
        n-=1
    return Answer

def nPr(n,r):
    Answer=1
    while r>0:
        Answer*=n
        r-=1
        n-=1
    return Answer

def GetPermutation(n,r,PermutationID):
    if n<r: return "LOGIC ERROR: r>n"
    if PermutationID>=nPr(n,r): return "LOGIC ERROR: PermutationID OFF Range"
    CurrentPermutation,LastPermutation = list(""), list("")
    for i in range(r):
        CurrentPermutation+=chr(i+49)
        LastPermutation+=chr(n-i+48)
    CurrentPermutationID=0
    while 1:
        if PermutationID==CurrentPermutationID: return "".join(CurrentPermutation)
        if CurrentPermutation==LastPermutation: break
        i=r
        while i>=0:
            i-=1
            DigitsOnTheRight = list("")
            for ii in range(n):
                ThisDigitIsOnTheRight=True
                for iv in range(i+1):
                    if (ii+1+48)==ord(CurrentPermutation[iv]):
                        ThisDigitIsOnTheRight=False
                        break
                if ThisDigitIsOnTheRight: DigitsOnTheRight+=chr(ii+1+48)
            NextDigit=-1
            for ii in range(len(DigitsOnTheRight)):
                if CurrentPermutation[i]<DigitsOnTheRight[ii]:
                    if NextDigit!=-1 and DigitsOnTheRight[NextDigit]<DigitsOnTheRight[ii]: None 
                    else: NextDigit=ii
            if NextDigit!=-1:
                TempCP=CurrentPermutation[i]
                CurrentPermutation[i]=DigitsOnTheRight[NextDigit]
                DigitsOnTheRight[NextDigit]=TempCP
                NewDigitsOnTheRight = list("")
                LastChar=chr(0)
                for ii in range(len(DigitsOnTheRight)):
                    MinValue=chr(127)
                    for iv in range(len(DigitsOnTheRight)):
                        if DigitsOnTheRight[iv]>LastChar and DigitsOnTheRight[iv]<MinValue:
                            MinValue=DigitsOnTheRight[iv]
                    LastChar=MinValue
                    NewDigitsOnTheRight+=LastChar
                DigitsOnTheRight=NewDigitsOnTheRight
                for ii in range(i+1,r):
                    CurrentPermutation[ii]=DigitsOnTheRight[ii-i-1]
                break
        CurrentPermutationID+=1




def PrintAllPossiblePermutations(n,r):
    # first permutation is {n[0],n[1],n[2],n[3]...n[r-1]}
    # last permutation is {n[n.size()-1],n[n.size()-2],n[n.size()-3]...n[n.size()-r]}
    CurrentPermutation,LastPermutation = list(""), list("")
    for i in range(r):
        CurrentPermutation+=chr(i+49)
        LastPermutation+=chr(n-i+48)
    while 1:
        print "".join(CurrentPermutation)
        if CurrentPermutation==LastPermutation:break
        #increment
        for i in range(r-1,-1,-1):
        #check if CurrentPermutation[i] is less than one of the digits on its right
            DigitsOnTheRight = list("")
            for ii in range(n):
                #if( the number (ii+1+48) is not in the string  (CurrentPermutation[0]-CurrentPermutation[i]) inclusively
                     #, then add it to DigitsOnTheRight
                ThisDigitIsOnTheRight=True
                for iv in range(i+1):
                    if (ii+1+48)==ord(CurrentPermutation[iv]):
                        ThisDigitIsOnTheRight=False
                        break
                if ThisDigitIsOnTheRight: DigitsOnTheRight+=chr(ii+1+48)
            #if( one of the DigitsOnTheRight is greater than CurrentPermutation[i] )
                 #,then replace CurrentPermutation[i] by the smallest DigitOnTheRight that is greater than CurrentPermutation[i];
                 # and replace that DigitOnTheRight by CurrentPermutation[i] ie. exchange CurrentPermutation[i] and the next DigitOnTheRight
                 # and then rearrange DigitsOnTheRight in an ascending order (the smallest on the left) and use them to replace the characters on the range (CurrentPermutation[i+1]-CurrentPermutation[r-1]) inclusively
                 # and break
            NextDigit=-1
            for ii in range(len(DigitsOnTheRight)):
                if CurrentPermutation[i]<DigitsOnTheRight[ii]:
                    if NextDigit!=-1 and DigitsOnTheRight[NextDigit]<DigitsOnTheRight[ii]:None
                    else: NextDigit=ii
            if NextDigit!=-1:
                #then this digit is increasable
                TempCP=CurrentPermutation[i];
                #exchange
                CurrentPermutation[i]=DigitsOnTheRight[NextDigit]
                DigitsOnTheRight[NextDigit]=TempCP
                #rearrange DigitsOnTheRight in an ascending order;
                NewDigitsOnTheRight = list('')
                LastChar=chr(0)
                for ii in range(len(DigitsOnTheRight)):
                    MinValue=chr(127)
                    for iv in range(len(DigitsOnTheRight)):
                        if DigitsOnTheRight[iv]>LastChar and DigitsOnTheRight[iv]<MinValue:
                            MinValue=DigitsOnTheRight[iv]
                    LastChar=MinValue
                    NewDigitsOnTheRight+=LastChar
                DigitsOnTheRight=NewDigitsOnTheRight
                #insert them on the range (CurrentPermutation[i+1]-CurrentPermutation[r-1]) inclusively
                for ii in range(i+1,r):
                    CurrentPermutation[ii]=DigitsOnTheRight[ii-i-1]
                break




#Testing Example

while 1:
    inp = map(int, raw_input("\nnPr, Enter n,r separated by space : ").split())
    n,r = inp[0], inp[1]
    del inp
    if r>n : print "LOGIC ERROR: (r>n)"
    else:
        print "\n", n, "P", r, "=", nPr(n,r)
        inp = raw_input("Print all possible permutations? (y,n) : ")
        if inp=='y': PrintAllPossiblePermutations(n,r)
        del inp
        raw_input()
        PID = long(raw_input("\nGetPermutation : PermutationID = "))
        print "\nPermutation[", PID, "]=", GetPermutation(n,r,PID)
        print "\n\n\n\n"
