#problem (codewars)
"""
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
"""

#What I think I gonna do
"""
to create a key for all digit value in base 10, centenar and million
to create a function that will take a string and return the integer value
that funtion split the string for ' ' and comparated in the dict
"""

#First implementation
def parse_int(string: str) -> int:
   diccionario = {
      "zero": 0, "one": 1, "two": 2,
      "three": 3, "four": 4, "five": 5,
      "six": 6, "seven": 7, "eight": 8,
      "nine": 9, "ten": 10, "eleven": 11,
      "twelve": 12, "thirteen": 13, "fourteen": 14, 
      "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
      "nineteen": 19, "twenty": 20, "thirty": 30,
      "forty": 40, "fifty": 50, "sixty": 60,
      "seventy": 70, "eighty": 80, "ninety": 90,
      "hundred": 100, "thousand": 1000, "million": 1000000
   }
   values = []
   value = 0
   for word in string.replace(' and ', ' ').split():
      try:
         if '-' in word:
            v = word.split('-')
            val = diccionario.get(v[0]) + diccionario.get(v[1])
            values.append(val)
            continue

         if word in ['hundred', 'thousand', 'million']:
            if word == 'thousand' or word == 'million':
               value += values.pop()
               value *= diccionario.get(word)
            
            if word == 'hundred':
               val = values.pop() * diccionario.get(word)
               value += val
            # continue 26000 + (300 * 100)
         else:
            values.append(diccionario.get(word))
      except IndexError as e:
         print(f"Error: {e}")
         value *= diccionario.get(word)


   if values:
      value += values.pop()
   
   return value



#clean code
"""
Naaiii, me rehuso🥱
"""

# print(parse_int('one'))
# print(parse_int('twenty'))
# print(parse_int('two hundred forty-six'))
print(parse_int('seven hundred thousand'))
# print(parse_int('four hundred ninety-three thousand seven hundred forty-three'))
# print(parse_int('three hundred eighty-nine thousand two hundred twenty-three'))
# print(parse_int('twenty-six thousand three hundred and fifty-nine'))