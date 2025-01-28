#problem (Mouredev)
"""
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""

#First implementation
def maxC_div_and_minC_mul(a, b):
   a = a if a > 0 else a * -1
   b = b if b > 0 else b * -1
   def MCD(a, b):
      if b == 0:
         return a
      return MCD(b, a%b)

   def MCM(a, b, mcd):
      return (a * b) // mcd
   
   mcd = MCD(a, b)
   mcm = MCM(a, b, mcd)

   return mcd, mcm

#clean code
print(maxC_div_and_minC_mul(-18, 48))
print(maxC_div_and_minC_mul(30, 66))
print(maxC_div_and_minC_mul(8, 100))