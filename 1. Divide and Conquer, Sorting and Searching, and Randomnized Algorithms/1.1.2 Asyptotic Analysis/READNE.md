# 1.1.2 Asyptotic Analysis
## The Gist
Why study the vocabulary for algorithm and asymptotic analysis?
![](1.Motivation.png)
The idea is to suppress constant factors and low-order terms.
Three examples are given:
	1. One Loop: O(n)
	2. Two Loops: O(n)
	3. Two Nested Loops: O(n^2)
## Definition of the Big-O Notation
![](2.Big-Oh.png)
That is to say, if we want to verify if T(n) = O(f(n)), we need to find two independent constants x0 and c, such that for arbitrary x>=x0, T(n) <=c*O(f(n)).  
### Examples
1. ![](3.Big-Oh-1.png)
2. ![](4.Big-Oh-2.png)
## Omega & Theta Notations
1. Omega Notation: the algorithm's running time is bounded below.
![](5.Omega.png)
2. Theta Notation: similar to the sandwich theorem, the running time of the algorithm is bounded in between.
![](6.Theta.png)
3. Little-Oh Notation
![](7.Little-Oh.png)
Few examples are given afterwards.

