"""
Your goal in this kata is to implement a difference function, 
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.
array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]
"""

# what I think I gonna do
"""
Ill take 2 list, and compare if iterable in a is in b -> a.remove(i)
"""

#first implementation
"""
def array_diff(a: list, b: list) -> list:
   if a == [] or b == []:
      return a
   for element in a.copy():
      # print(element in b)
      if element in b:
         a.remove(element)
         continue

   return a
"""

#clean code

def array_diff(a: list, b: list) -> list:
   return [element for element in a if element not in b]

# print(array_diff([1, 2, 2, 3], [2]))