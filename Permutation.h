#include <iostream>

unsigned long Factorial(unsigned n);
unsigned long nPr(unsigned n, unsigned r);
void PrintAllPossiblePermutations(unsigned char n, unsigned char r);

unsigned long Factorial(unsigned n)
{
    unsigned long Answer=1;
    while(n>1)
    {
        Answer*=n;
        n--;
    }
    return Answer;
}

unsigned long nPr(unsigned n, unsigned r)
{
    unsigned long Answer=1;
    for(; r>0; r--,n--)
    {
        Answer*=n;
    }
    return Answer;
}

std::string GetPermutation(unsigned char n, unsigned char r, unsigned long PermutationID /*base zero*/)
{
    if(n<r)return "LOGIC ERROR: r>n";
    if(PermutationID>=nPr(n,r)) return "LOGIC ERROR: PermutationID OFF Range";
    std::string CurrentPermutation,LastPermutation;
    for(unsigned i=0; i<r; i++)
    {
        CurrentPermutation+=(char)(i+49);
        LastPermutation+=(char)(n-i+48);
    }
    unsigned long CurrentPermutationID=0;
    while(1)
    {
        if(PermutationID==CurrentPermutationID)return CurrentPermutation;
        if(CurrentPermutation==LastPermutation)break;
        for(int i=r-1; i>=0; i--)
        {
            std::string DigitsOnTheRight;
            for(int ii=0; ii<n; ii++)
            {
                bool ThisDigitIsOnTheRight=1;
                for(int iv=0; iv<=i; iv++)
                    if((ii+1+48)==CurrentPermutation[iv])
                    {
                        ThisDigitIsOnTheRight=0;
                        break;
                    }
                if(ThisDigitIsOnTheRight)DigitsOnTheRight+=(char)(ii+1+48);
            }
            int NextDigit=-1;
            for(int ii=0; ii<DigitsOnTheRight.size(); ii++)
                if(CurrentPermutation[i]<DigitsOnTheRight[ii])
                {
                    if(NextDigit!=-1&&DigitsOnTheRight[NextDigit]<DigitsOnTheRight[ii]);
                    else NextDigit=ii;
                }
            if(NextDigit!=-1)
            {
                char TempCP=CurrentPermutation[i];
                CurrentPermutation[i]=DigitsOnTheRight[NextDigit];
                DigitsOnTheRight[NextDigit]=TempCP;
                std::string NewDigitsOnTheRight;
                char LastChar=0;
                for(int ii=0; ii<DigitsOnTheRight.size(); ii++)
                {
                    char MinValue=127;
                    for(int iv=0; iv<DigitsOnTheRight.size(); iv++)
                        if(DigitsOnTheRight[iv]>LastChar&&DigitsOnTheRight[iv]<MinValue)
                            MinValue=DigitsOnTheRight[iv];
                    LastChar=MinValue;
                    NewDigitsOnTheRight+=LastChar;
                }
                DigitsOnTheRight=NewDigitsOnTheRight;
                for(int ii=i+1; ii<r; ii++)
                    CurrentPermutation[ii]=DigitsOnTheRight[ii-i-1];
                break;
            }
        }
        CurrentPermutationID++;
    }
}

void PrintAllPossiblePermutations(unsigned char n, unsigned char r)//(unsigned char n, unsigned char r)
{
    // first permutation is {n[0],n[1],n[2],n[3]...n[r-1]}
    // last permutation is {n[n.size()-1],n[n.size()-2],n[n.size()-3]...n[n.size()-r]}
    std::string CurrentPermutation,LastPermutation;
    for(unsigned i=0; i<r; i++)
    {
        CurrentPermutation+=(char)(i+49);
        LastPermutation+=(char)(n-i+48);
    }
    // increment algorithm is
    while(1)
    {
        std::cout<<CurrentPermutation<<std::endl;
        if(CurrentPermutation==LastPermutation)break;
        //increment
        for(int i=r-1; i>=0; i--)
        {
        //check if CurrentPermutation[i] is less than one of the digits on its right
            std::string DigitsOnTheRight;
            for(int ii=0; ii<n; ii++)
            {
                //if( the number (ii+1+48) is not in the string  (CurrentPermutation[0]-CurrentPermutation[i]) inclusively
                     //, then add it to DigitsOnTheRight
                bool ThisDigitIsOnTheRight=1;
                for(int iv=0; iv<=i; iv++)
                    if((ii+1+48)==CurrentPermutation[iv])
                    {
                        ThisDigitIsOnTheRight=0;
                        break;
                    }
                if(ThisDigitIsOnTheRight)DigitsOnTheRight+=(char)(ii+1+48);
            }
            //if( one of the DigitsOnTheRight is greater than CurrentPermutation[i] )
                 //,then replace CurrentPermutation[i] by the smallest DigitOnTheRight that is greater than CurrentPermutation[i];
                 // and replace that DigitOnTheRight by CurrentPermutation[i] ie. exchange CurrentPermutation[i] and the next DigitOnTheRight
                 // and then rearrange DigitsOnTheRight in an ascending order (the smallest on the left) and use them to replace the characters on the range (CurrentPermutation[i+1]-CurrentPermutation[r-1]) inclusively
                 // and break
            int NextDigit=-1;
            for(int ii=0; ii<DigitsOnTheRight.size(); ii++)
                if(CurrentPermutation[i]<DigitsOnTheRight[ii])
                {
                    if(NextDigit!=-1&&DigitsOnTheRight[NextDigit]<DigitsOnTheRight[ii]);
                    else NextDigit=ii;
                }
            if(NextDigit!=-1)
            {
                //then this digit is increasable
                char TempCP=CurrentPermutation[i];
                //exchange
                CurrentPermutation[i]=DigitsOnTheRight[NextDigit];
                DigitsOnTheRight[NextDigit]=TempCP;
                //rearrange DigitsOnTheRight in an ascending order;
                std::string NewDigitsOnTheRight;
                char LastChar=0;
                for(int ii=0; ii<DigitsOnTheRight.size(); ii++)
                {
                    char MinValue=127;
                    for(int iv=0; iv<DigitsOnTheRight.size(); iv++)
                        if(DigitsOnTheRight[iv]>LastChar&&DigitsOnTheRight[iv]<MinValue)
                            MinValue=DigitsOnTheRight[iv];
                    LastChar=MinValue;
                    NewDigitsOnTheRight+=LastChar;
                }
                DigitsOnTheRight=NewDigitsOnTheRight;
                //insert them on the range (CurrentPermutation[i+1]-CurrentPermutation[r-1]) inclusively
                for(int ii=i+1; ii<r; ii++)
                    CurrentPermutation[ii]=DigitsOnTheRight[ii-i-1];
                break;
            }
        }
    }
}
