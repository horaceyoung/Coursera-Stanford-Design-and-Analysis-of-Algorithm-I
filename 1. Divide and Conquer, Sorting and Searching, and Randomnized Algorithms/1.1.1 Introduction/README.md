# 1.1.1 Introduction
## Karatsuba Multiplication
The lecturer introduced the topic of algorithm with a simple algorithm - the multiplication of 2 integers, namely x and y.  
The process is simple: we take the least significant digit of the multiplier, multiply each digit with its corresponding weight and add the result together.  
We shift the multiplier digit to the left by one digit and perform the same process for all digits of the multiplier. In the end the operations in total is proportional to n^2.  
But we have better alternatives and here is one: the Karatsuba Multiplication.  

![](images/1.1.1/Karatsuba.png)
##Expanation
The process is as following:  
Firstly we split the multiplier and multiplicand into half each, (e.g. 1234 into 12 and 34, if is an odd-digit number like 12345, we can split it into 123 and 45), name them a, b, c, and d respectively:  
x = 10^(n/2)*a +b, y = 10^(n/2)c+d  

then we do the following:    
	1. Recursively compute ac
	2. recursively compute bd
	3. recursively compute (a+b)(c+d) and derive ad+bc  


x*y = 10^n * ac + 10^(n/2)(ad+bc) + bd  
![](images/1.1.1/Kratsuba2.png)