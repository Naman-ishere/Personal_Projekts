

**Problem Overview :** 

**ARMSTRONG NUMBER** : 

Such type of numbers whose sum of cubes of each digit is equal to the number itself. 
e.g. 153 --> (1)^3 + (5)^3 + (3)^3 = 1 + 125 + 27 = 153

**Structure of Problem** : 

1. Take the input from the user.
2. Divide the digits in individual numbers.
3. Raise each number to 3 and find the sum of them.
4. If sum == input, then the number Armstrong Number.

**Pseudocode** :

START 
	INPUT n
	 CHANGE TYPE n = STRING
	 



**DRY RUN** :

n = user input
m = n
while n > 0:
    d = n % 10
     r = r  * 10 + d
     n = n // 10
