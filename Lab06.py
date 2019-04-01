import math

class Geometric_Calculator_Triangle:
  def __init__(self, side1, side2, side3):
    self.polygon = "Triangle"
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
  def calculate_triangle_perimeter(self):
      print ('\nThis is the Triangle perimeter: ') 
      return self.side1+self.side2+self.side3
  def calculate_triangle_area(self):
      p = self.calculate_triangle_perimeter()/2
      equation = p*(p-self.side1)*(p-self.side2)*(p-self.side3)
      area = math.sqrt(equation)
      print ('\nThis is the Triangle area: ') 
      return area

class Rect_Calc:
  def __init__(self, side1, side2):
    self.polygon = "Rectangle"
    self.side1 = side1
    self.side2 = side2
  def calc_rect_perimeter(self):
      print ('\nThis is the Rectangle perimeter: ') 
      return self.side1+self.side1+self.side2+self.side2
  def calc_rect_area(self):
      print ('\nThis is the Rectangle area: ') 
      return self.side1*self.side2

class Diamond_Calc:
  def __init__(self, side1):
    self.polygon = "Diamond"
    self.side1 = side1
  def calc_diamond_perimeter(self):
      print ('\nThis is the Diamond perimeter: ') 
      return self.side1*4
  def calc_diamond_area(self):
      print ('\nThis is the Diamond area: ')#I assumed that the bottom angle "V" of the diamond to be 30 degrees
      return (self.side1*6.928)+(self.side1*0.067)
      
gc = Geometric_Calculator_Triangle(3, 4, 5)
print (gc.calculate_triangle_perimeter())
print (gc.calculate_triangle_area())
gc.side1 = 6
print (gc.calculate_triangle_perimeter())
print (gc.calculate_triangle_area())
gd = Rect_Calc(5, 8)
print (gd.calc_rect_perimeter())
print (gd.calc_rect_area())
gd.side1 = 22
print (gd.calc_rect_perimeter())
print (gd.calc_rect_area())
gf = Diamond_Calc(7)
print (gf.calc_diamond_perimeter())
print (gf.calc_diamond_area())
gf.side1 = 13
print (gf.calc_diamond_perimeter())
print (gf.calc_diamond_area())
