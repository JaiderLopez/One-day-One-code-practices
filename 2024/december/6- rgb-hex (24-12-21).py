#problem from codewars
"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result 
in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. 
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""

#What I think I gonna do
"""
to validate 'r', 'g', 'b' in the range
create a dict hexadecimal characters
create a function to convert decimal to hexadecimal
"""

#First implementation
"""

def rgb(r, g, b) -> str:
   hex_dict = {
      0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
      5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
      10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
      15: 'F'
   }
   def validate(rgb: list):
      return [x if 0 <= x <= 255 else (0 if x < 0 else 255) for x in rgb]

   hexadecimal = ''
   values = validate([r, g, b])
   for v in values:
      hexadecimal += hex_dict[v // 16] + hex_dict[v % 16]
   return hexadecimal
"""
#clean code
def rgb(r: int, g: int, b: int) -> str:
   def validate(value: int) -> int:
      return max(0, min(255, value))
   
   return f"{validate(r):02X}{validate(g):02X}{validate(b):02X}"


print(rgb(-20, 275, 125))