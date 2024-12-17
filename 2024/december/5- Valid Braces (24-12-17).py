#problem
"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. 
It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], 
and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.
"""

#What I think I gonna do
"""
create a dict with close brace like key and open brace like value
creating a stack to contein all open braces in the str and pop with correct close brace
"""

#First implementation
"""

def valid_braces(string):
   braces: dict = {
      ')': '(',
      ']': '[',
      '}': '{',
   }
   stack: list = []
   for brace in list(string):
      if brace in braces:
         try:
            if not stack.pop() == braces[brace]:
               return False
         except Exception:
            return False
      else:
         stack.append(brace)
   return True if stack == [] else False
"""

#clean code
def valid_braces(string: str) -> bool:
   braces: dict = { ')': '(', ']': '[', '}': '{' }
   stack: list = []

   for brace in string:
      if brace in braces:
         if not stack or stack.pop() != braces[brace]:
               return False
      else:
         stack.append(brace)
   
   return not stack


print(valid_braces('{}({})[]'))
