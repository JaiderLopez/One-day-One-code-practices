#problem
"""
How many ways can you make the sum of a number?
From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)

In number theory and combinatorics, a partition of a positive integer n, 
also called an integer partition, is a way of writing n as a sum of positive integers. 
Two sums that differ only in the order of their summands are considered the same partition. 
If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
"""

#First implementation
def exp_sum(n):
   current_list = [1] + [0] * n

   for i in range(1, n + 1):
      for j in range(i, n + 1):
         current_list[j] += current_list[j - i]
         # print(current_list)
   return current_list[n]


print(exp_sum(5))