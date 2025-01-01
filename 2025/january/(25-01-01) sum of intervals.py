#problem (codewars)
"""
Write a function called sumIntervals/sum_intervals that accepts an array of intervals, 
and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. 
The first value of the interval will always be less than the second value. Interval example: 
[1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1, 4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, 
we can treat the interval as [1, 5], which has a length of 4.
"""

#What I think I gonna do
"""
to order intervals by first value
then to iterate over intervals and add their lengths to the sum if not overlapping
else: capture min and max between overlapping intervals
"""

#First implementation
def sum_intervals(intervals):
   if not intervals:
      return 0

   intervals.sort(key = lambda x: x[0])

   total_length = 0
   current_start, current_end = intervals[0]

   for start, end in intervals[1:]:
      if start <= current_end:
         current_end = max(current_end, end)
      else:
         total_length += current_end - current_start
         current_start, current_end = start, end
   total_length += current_end - current_start

   return total_length

# Ejemplos de uso
# print(sum_intervals([[1, 2], [6, 10], [11, 15]]))  # Salida: 9
# print(sum_intervals([[1, 4], [7, 10], [3, 5]]))   # Salida: 7
print(sum_intervals([[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]))  # Salida: 19
# print(sum_intervals([[1, 5]]))  # 4
# print(sum_intervals([[0, 20], [-100000000, 10], [30, 40]]))  # Salida: 100000030



#clean code
# not needed
