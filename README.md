# Permuter
Extensible high performance permutation algorithms for effectively generating posibilities.
##Content
 - [**Permutation.h**](#permutationh)
  - [Factorial(n);](#factorialn)
  - [nPr(n,r);](#nprnr)
  - [PrintAllPossiblePermutations(n,r);](#printallpossiblepermutationsnr)
  - [GetPermutation(n,r,PermutationID);](#getpermutationnrpermutationid)
 - [**PrintAllPossibleStrings.h**](#printallpossiblestringsh)
  - [PrintAllPossibleCombinations(PossibleDigits,Length);](#printallpossiblecombinationspossibledigitslength)
  
##**Permutation.h**

<br></br>

###Factorial(n);
A simple function for calculating the factorial of a number.
####Syntax
```C++
unsigned long Factorial(unsigned n);
```
####Parameters
 - unsigned **n**
 
 A number to calculate its factorial.
 
####Return value
 - unsigned long
 
 The value of factorial **n**
 
<br></br>
<br></br>
 
 
###nPr(n,r);
A simple function for calculating number of possible subsets of **r** elements from a set of **n** elements.
####Syntax
```C++
unsigned long nPr(unsigned n, unsigned r);
```
####Parameters
 - unsigned **n**
 
 Number of elements to be permuted.
 - unsigned **r**
 
 Number of elements for each ordered subset.
 
####Return value
 - unsigned long
 
 The number of possible permutations of a subset of r elements from a set of n elements.
 
<br></br>
<br></br>
 
 
###PrintAllPossiblePermutations(n,r);
A function that prints all possible permutations of **n** elements ordered in a subset of **r** elements.
####Syntax
```C++
void PrintAllPossiblePermutations(unsigned char n, unsigned char r);
```
####Parameters
 - unsigned char **n**
 
 Number of elements to be permuted.
 - unsigned char **r**
 
 Number of elements for each ordered subset.
 
####Return value
 - No return value.

<br></br>
<br></br>


###GetPermutation(n,r,PermutationID);
A function that directly generates the permutation number **PermutationID** of **n** elements ordered in a subset of **r** elements.
####Syntax
```C++
std::string GetPermutation(unsigned char n, unsigned char r, unsigned long PermutationID /*base zero*/);
```
####Parameters
 - unsigned char **n**
 
 Number of elements to be permuted.
 - unsigned char **r**
 
 Number of elements for each ordered subset.
 - unsigned long **PermutationID**
 
 Disposition of a permutation to be generated. (must be between zero and nPr-1 inclusively)
 
####Return value
 - The generated permutation in the form of ASCII encoded string. (if **n** is greater than 9 it generates non-decimal characters)

<br></br>
<br></br>


##**PrintAllPossibleStrings.h**

<br></br>

###PrintAllPossibleCombinations(PossibleDigits,Length);
A function that prints all possible strings of size **Length** where each character may hold any value of **PossibleDigits**. (the same value can be repeated).
####Syntax
```C++
void PrintAllPossibleCombinations(std::string PossibleDigits, unsigned long Length)
```
####Parameters
 - std::string **PossibleDigits**
 
 A string containing representative characters for all possible values the generated characters.
 Example: "01" for binary, "01234567" for octal, or "0123456789ABCDEF" for hexadecimal.
 - unsigned long **Length**
 
 Number of digits/characters in the generated numbers/strings.
 
####Return value
 - No return value.
