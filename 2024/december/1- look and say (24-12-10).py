# problem (codewars)
"""
Task
Get the digits sum of nth number from the Look-and-Say sequence(1-based).
1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...

The sum of digits in nth number from the Look-and-Say sequence.

Example
For n = 2, the output should be 2.
"11" --> 1 + 1 --> 2
For n = 3, the output should be 3.
"21" --> 2 + 1 --> 3
For n = 4, the output should be 5.
"1211" --> 1 + 2 + 1 + 1 --> 5
"""

# what I think I gonna do
"""
A function with 2 functions inside {{1}{2} code return} 
first to count numbers repeats {str count return []}
and other to write this result in the number to return{list traslete return str}
"""

# first implementation
"""def look_and_say_and_sum(n: int) -> str:
   if not 1 <= n <= 55:
      return
   lista: str = ""
   def separate(lista: str):
      #"21"
      val = None
      store = []
      to_return = []
      for l in lista: #2 1
         # if i == 4:
         #    print(":::", l)
         #    print(val)
         if val == None:
            val = l
            store.append(l)
         elif l == val:
            store.append(l)
         else:
            val = l
            to_return.append(store)
            store = []
            store.append(l)
      to_return.append(store)
      return to_return

   def count(lista: list) -> str:
      to_return: str = ""
      for l in lista:
         #[[1], [2], [1, 1]]
         val = l[0]
         count = l.count(val)
         to_return += str(count) + str(val)
      return to_return
   
   def suma_total(lista: str)-> int:
      lista = list(lista)
      return sum(map(lambda x: int(x), lista))

   lista+="1"
   if n == 1:
      return 1
   i = 2
   while i <= n:
      datos = separate(lista)
      lista = count(datos)
      i += 1

   
   return suma_total(lista)

print(look_and_say_and_sum(55))
"""

# clean code

def look_and_say_and_sum(n: int) -> int:
   if not 1 <= n <= 55:
      return 0  # return 0 if out of the range

   def separate(sequence: str) -> list:
      groups = []
      current_group = [sequence[0]]

      for char in sequence[1:]:
         if char == current_group[-1]:
               current_group.append(char)
         else:
               groups.append(current_group)
               current_group = [char]

      groups.append(current_group)
      return groups

   def count(groups: list) -> str:
      return ''.join(f"{len(group)}{group[0]}" for group in groups)

   def suma_total(sequence: str) -> int:
      return sum(map(int, sequence))

   sequence = "1"

   for _ in range(1, n):
      groups = separate(sequence)
      sequence = count(groups)

   return suma_total(sequence)
