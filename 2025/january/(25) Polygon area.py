#problem (Mouredev)
"""
   * Crea una única función (importante que sólo sea una) que sea capaz
   * de calcular y retornar el área de un polígono.
   * - La función recibirá por parámetro sólo UN polígono a la vez.
   * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
   * - Imprime el cálculo del área de un polígono de cada tipo.
"""

#First implementation
class Polygon:
   def __init__(self, base):
      self.base = base
      
   
   def aarea(self):
      return self.area

class Triangle(Polygon):
   def __init__(self, base, height):
      super().__init__(base)
      self.height = height
      self.area = self.base * self.height * 0.5

class Square(Polygon):
   def __init__(self, base):
      super().__init__(base)
      self.area = self.base * self.base

class Rectangle(Polygon):
   def __init__(self, base, height):
      super().__init__(base)
      self.height = height
      self.area = self.base * self.height

def polygon_area(polygon: Polygon):
   return polygon.aarea()

print(polygon_area(Triangle(10, 5)))
print(polygon_area(Square(10)))
print(polygon_area(Rectangle(10, 5)))