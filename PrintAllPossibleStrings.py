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



def PrintAllPossibleCombinations(PossibleDigits,Length):
    PossibleDigits = list(PossibleDigits)
    CurrentSequence,LastSequence = list(""), list("")
    for i in range(Length):
        CurrentSequence+=PossibleDigits[0]
        LastSequence+=PossibleDigits[len(PossibleDigits)-1]

    while 1:
        print "".join(CurrentSequence)
        if CurrentSequence==LastSequence: break
        #increment
        i=Length
        while 1: #see all digits starting from the least significant
            i-=1
            #get the value of the current digit
            digit_value=-1
            while digit_value<len(PossibleDigits):
                digit_value+=1
                if CurrentSequence[i]==PossibleDigits[digit_value]:
                    break
            #if(the current digit is less than the maximum value of a digit), increment it to the next value and break;
            if digit_value<len(PossibleDigits)-1:
                CurrentSequence[i]=PossibleDigits[digit_value+1]
                break
            #else, change it to the first/least/zero value and continue to see the next digit;
            else : CurrentSequence[i]=PossibleDigits[0]
            if not i: break



#Testing Example
PossibleValues = ""
Length = 0
while 1:
    print "Enter a string of all possible values of a digit in the number in ascending order\n"
    print "Example: \"0123456789ABCDEF\" for hexadecimal, \"01\" for binary, etc..."
    PossibleValues = raw_input()
    print "Enter the length of the number (number of digits)\n"
    Length = int(raw_input())
    PrintAllPossibleCombinations(PossibleValues,Length)
    raw_input() #Prevent the application from closing immediately
