#problem (codewars)
"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters 
after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating
"""

#What I think I gonna do
"""
import string 
to get index value iterating the text parameter and compare it with ascii_letters from string library
then sum 13 at index and calculate mod 26
"""

#First implementation
"""
from string import ascii_lowercase, ascii_uppercase
def rot13(message):
   result = ""
   def transform(i, tipo, result):
      i = (i + 13) % 26
      result += tipo[i]
      return result

   for letter in message:
      if not letter.isalpha():
         result += letter
         continue
      if letter in ascii_lowercase:
         i = ascii_lowercase.index(letter)
         result = transform(i, ascii_lowercase, result)
      else:
         i = ascii_uppercase.index(letter)
         result = transform(i, ascii_uppercase, result)
      

   return result
"""
#clean code
from string import ascii_lowercase, ascii_uppercase

def rot13(message):
   result = []
   
   def transform(letter, alphabet):
      index = (alphabet.index(letter) + 13) % 26
      return alphabet[index]
   
   for letter in message:
      if letter in ascii_lowercase:
         result.append(transform(letter, ascii_lowercase))
      elif letter in ascii_uppercase:
         result.append(transform(letter, ascii_uppercase))
      else:
         result.append(letter)
   
   return ''.join(result)

# I liked this one
"""
def rot13(message):
   return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))
"""
print(rot13('Hola Mundo'))
print(rot13('test'))
