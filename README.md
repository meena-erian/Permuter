# Permuter
Extensible hight performance permutation algorithms for effectively generating posibilities
##Content
 - Permutation.h
  - ```C++
  unsigned long Factorial(unsigned n);
  ```
  - unsigned long nPr(unsigned n, unsigned r);
  - void PrintAllPossiblePermutations(unsigned char n, unsigned char r);
  - std::string GetPermutation(unsigned char n, unsigned char r, unsigned long PermutationID /*base zero*/);
 - PrintAllPossibleStrings.h
  - void PrintAllPossibleCombinations(std::string PossibleDigits, unsigned long Length);
