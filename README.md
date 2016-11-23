# Permuter
Extensible hight performance permutation algorithms for effectively generating posibilities
##Content
 - [**Permutation.h**](#permutationh)
  - [Factorial(n);](#factorialn)
  - [nPr(n,r);](#nprnr)
  - [PrintAllPossiblePermutations(n,r);](#printallpossiblepermutationsnr)
  - [GetPermutation(n,r,PermutationID);](#getpermutationnrpermutationid)
 - [**PrintAllPossibleStrings.h**](#printallpossiblestringsh)
  - [PrintAllPossibleCombinations(PossibleDigits,Length);](#printallpossiblecombinationspossibledigitslength)
  
##**Permutation.h**
###Factorial(n);
####Syntax
A simple function for calculating the factorial of a number
```C++
unsigned long Factorial(unsigned n);
```
####Parameters
 - unsigned n
 A number to calculate its factorial.
####Return value
 - unsigned long
 The value of factorial n
 
###nPr(n,r);
A simple function for calculating number of possible subsets of **r** elements from a set of **n** elements.
```C++
unsigned long nPr(unsigned n, unsigned r);
```
####Parameters
 - unsigned n
 Number of elements to be permuted.
 - unsigned r
 Number of elements for each ordered subset.
####Return value
 - unsigned long
 The number of possible permutations of a subset of r elements from a set of n elements.
 
###PrintAllPossiblePermutations(n,r);
###GetPermutation(n,r,PermutationID);
##**PrintAllPossibleStrings.h**
###PrintAllPossibleCombinations(PossibleDigits,Length);
