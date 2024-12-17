# problem (codewars)
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)
"""

# What I think I gonna do
"""
- take the number iteration below the parameter and compare if multiples of 3 or 5 to save
- if the number is negative, return 0
- if the number is a multiple of both 3 and 5, look if saved before
"""

#first implementation
"""
def solution(number: int) -> int:
   if number < 2:
      return 0
   sum = 0
   for i in range(1, number):
      if i % 3 == 0 and i % 5 == 0:
         sum += i
         continue
      if i % 3 == 0:
         sum+= i
         continue
      if i % 5 == 0:
         sum += i
         continue
   return sum
   """

# clean code
def solution(number):
   multiples = [x for x in range(number) if x % 3 == 0 or x % 5 == 0]
   return sum(multiples)
