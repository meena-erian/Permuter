#include "Permutation.h"

int main()
{
    unsigned n,r;
start:
    std::cout<<"\nnPr ";
    std::cin>>n>>r;
    if(r>n)std::cout<<"LOGIC ERROR: (r>n)\n";
    else
    {
        std::cout<<"\n"<<n<<"P"<<r<<"="<<nPr(n,r)<<std::endl;
        std::cout<<"Print all possible permutations? (y,n) : ";
        std::cin.get();
        if(std::cin.get()=='y')
        PrintAllPossiblePermutations(n,r);
        std::cin.get();
        std::cout<<"\nGetPermutation : PermutationID = ";
        unsigned long PID;
        std::cin>>PID;
        std::cout<<"\nPermutation["<<PID<<"]="<<GetPermutation(n,r,PID);
        std::cout<<"\n\n\n\n";
    }
goto start;
}
