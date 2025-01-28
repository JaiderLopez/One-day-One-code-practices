#problem (codewars)
"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans 
at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a 
correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

"""

#First implementation
"""def solution(args):
   result = ''
   current = []
   for i in args:
      if not current:
         current.append(i)
         continue
      if i == current[-1] + 1:
         current.append(i)
      else:
         if len(current) > 2:
            result += str(current[0]) +'-'+ str(current[-1]) + ','
            current = [i]
         else:
            result += ','.join(map(str, current)) + ','
            current = [i]
   if len(current) > 2:
      result += str(current[0]) +'-'+ str(current[-1])
   else:
      result += ','.join(map(str, current)) + ','
      current = [i]
   if result[-1] == ',':
      result = result[:-1]
   return result
"""
#clean code
def solution(args):
   result = []
   current = []

   for i in args:
      if not current or i == current[-1] + 1:
         current.append(i)
      else:
         if len(current) > 2:
            result.append(f"{current[0]}-{current[-1]}")
         else:
            result.extend(map(str, current)) #max 2 numbers in current
         current = [i]

   if len(current) > 2:
      result.append(f"{current[0]}-{current[-1]}")
   else:
      result.extend(map(str, current))

   return ','.join(result)

print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))