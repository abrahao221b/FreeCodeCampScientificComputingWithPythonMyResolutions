from typing import overload
from typing_extensions import override
import math

# Class Rectangle
class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  # Sets
  
  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  # Function that calculates the rectangle's area 
  def get_area(self):
    return self.width * self.height

  # Function that calculates the rectangle's perimeter 
  def get_perimeter(self):
    return (self.width + self.height) * 2

  # Function that calculates the rectangle's diagonal 
  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)
  
  # Function that prints the rectangle  
  def get_picture(self):
    output = ""
    if self.height <= 50 and self.width < 50:
      for _ in range(self.height):
        for _ in range(self.width):
          output += "*"
        output += "\n"
    else:
      output += "Too big for picture."
    return output

  # Function that given a rectangle, calculates how many copies of it are needed to fill the instance object
  def get_amount_inside(self, rect):
    result = math.floor((self.width / rect.width) * (self.height / rect.height))
    if result < 1:
      return 0
    else:
      return result

  # Rectangle to string function 
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

# Class Square
class Square(Rectangle):

  def __init__(self, side_length):
    super().__init__(width=side_length, height=side_length)

  # Set 
  def set_side(self, value):
    super().set_height(value)
    super().set_width(value)

  # Function that calculates the square's area
  @override
  def get_area(self):
    return super().get_area()

  # Function that calculates the square's perimeter
  @override
  def get_perimeter(self):
    return super().get_perimeter()

  # Function that calculates the square's diagonal
  @override
  def get_diagonal(self):
    return super().get_diagonal()

  # Function that prints the square
  @override
  def get_picture(self):
    return super().get_picture()
    
  # Function that given a square, calculates how many of it are need to fill the instance object
  @override
  def get_amount_inside(self, rect):
    return super().get_amount_inside(rect)

  # Square to string function
  @override
  def __str__(self):
    return f"Square(side={self.width})"
