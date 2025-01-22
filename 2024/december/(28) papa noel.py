#problem
"""
EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 *
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 *
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 *
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
"""

#clean code
import random

def generar_codigo():
   """Genera un código secreto de 4 caracteres (A-C, 1-3) sin repeticiones."""
   letras = ['A', 'B', 'C']
   numeros = ['1', '2', '3']
   caracteres = letras + numeros
   codigo_secreto = random.sample(caracteres, 4)
   
   return ''.join(codigo_secreto)

def validar_intento(intento):
   """Valida que el intento tenga longitud 4 y contenga caracteres válidos."""
   if len(intento) != 4:
      return False, "El código debe tener exactamente 4 caracteres."
   
   if any(c not in ['A', 'B', 'C', '1', '2', '3'] for c in intento):
      return False, "El código solo puede contener A, B, C, 1, 2 y 3."
   
   return True, ""

def evaluar_intento(codigo_secreto, intento):
   """Evalúa el intento del usuario y devuelve los resultados."""
   resultado = []
   
   for i in range(4):
      if intento[i] == codigo_secreto[i]:
         resultado.append(f"{intento[i]}: Correcto")
      elif intento[i] in codigo_secreto:
         resultado.append(f"{intento[i]}: Presente")
      else:
         resultado.append(f"{intento[i]}: Incorrecto")
   
   return resultado

def juego():
   """Función principal del juego."""
   codigo_secreto = generar_codigo()
   intentos_restantes = 1
   
   print("*"*66) #66 porque noel es el diablo
   print("\t¡Bienvenido al juego de Papá Noel!")
   print("Tienes 10 intentos para adivinar el código secreto.")
   print("*"*66)
   
   while intentos_restantes > 0:
      intento = input("\nIntroduce tu código de 4 caracteres (A-C, 1-3): ").upper()
      
      valido, mensaje = validar_intento(intento)
      if not valido:
         print(mensaje)
         continue # "No está muy claro si se debe quitar un intento al jugador si es un codigo invalido"
      
      if intento == codigo_secreto:
         print("\n¡Felicidades! Has adivinado el código secreto. Papá Noel puede entregar los regalos.")
         break

      resultados = evaluar_intento(codigo_secreto, intento)
      for resultado in resultados:
         print(resultado)
      
      
      intentos_restantes -= 1
      print("*"*10,f"Te quedan {intentos_restantes} intentos.", "*"*10)
   
   if intentos_restantes == 0:
      print(f"Has agotado tus intentos \4. El código secreto era: {codigo_secreto}. Papá Noel no puede entregar los regalos.")

# Ejecutar el juego
if __name__ == "__main__":
    juego()
