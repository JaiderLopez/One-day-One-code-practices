#problem (codewars)
"""
There is a secret string which is unknown to you. Given a collection of random triplets from the string,
recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere 
before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that 
they contain sufficient information to deduce the original string. In particular, this means that the secret 
string will never contain letters that do not occur in one of the triplets given to you.
Example:
['t', 'u', 'p']
['w', 'h', 'i']
['t', 's', 'u']
['a', 't', 's']
['h', 'a', 'p']
secret: "what is up"
Input: triplets = [['t', 'u', 'p'], ['w', 'h','i'], ['t', 's', 'u'], ['a', 't', 's'], ['h', 'a', 'p']]
"""

#What I think I gonna do
"""

"""

#First implementation

def recover_secret(triplets) -> str:
   result = ''
   values = {}
   for triplet in triplets:
      for index, letter in enumerate(triplet):
         try:
            values[letter]+= index
         except KeyError:
            values[letter] = index

   values_current = values.copy()
   
   while values_current:
      val = []
      for letter in sorted(values_current):
         if values_current[letter] == 0:
            val.append(letter)
      if len(val) > 1:
         values_filter = {k: values[k] for k in val}
         next_letter = min(values_filter, key = values_filter.get)
      else: 
         next_letter = val.pop()
      
      result += next_letter

      for triplet in triplets:
         if next_letter in triplet:
            for letter in triplet:
               if letter in values_current:
                  if values_current[letter] == 0:
                     values_current.pop(letter, None)
                  else:
                     values_current[letter] -= 1
   return result


#clean code


triplets = [['t', 'u', 'p'], ['w', 'h','i'], ['t', 's', 'u'], ['a', 't', 's'], ['h', 'a', 'p']]
print(recover_secret(triplets))