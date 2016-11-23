#include "PrintAllPossibleStrings.h"

int main()
{
    std::string PossibleValues;
    unsigned long Length;
start:
    std::cout<<"Enter a string of all possible values of a digit in the number in ascending order\n";
    std::cout<<"Example: \"0123456789ABCDEF\" for hexadecimal, \"01\" for binary, etc...";
    getline(std::cin,PossibleValues);
    std::cout<<"Enter the length of the number (number of digits)\n";
    std::cin>>Length;
    PrintAllPossibleCombinations(PossibleValues,Length);
    std::cin.get();
goto start;
}
