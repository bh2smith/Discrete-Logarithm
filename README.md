# Discrete-Logarithm
A functioning implementation of the ``Big step, little step'' algorithm for computing discrete logs.

reads from STDIN as follows;
T = number of test cases

followed by T lines of:

a b g = numbers for which we seek to solve a^x = b mod g

Algorithm is functional for 1\leq g \leq 10^10 and operates in under 10 seconds when T \leq 10
