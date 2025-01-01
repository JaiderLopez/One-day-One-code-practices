#problem
"""
Given an n x n array, return the array elements arranged from outermost elements to the middle element, 
traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
"""

#What I think I gonna do
"""
...
"""

#First implementation
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

def snail(array):
   result = []
   while array:
      # left to right
      result.extend(array.pop(0))
      
      # top to bottom
      if array and array[0]:
         for col in array:
            result.append(col.pop())

      # right to left
      if array:
         result.extend(array.pop()[::-1])

      # bottom to top
      if array and array[0]:
         for col in array[::-1]:
            result.extend(array.pop(0))
      
   return result

print(snail(array))