class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __str__(self):
    return(("Rectangle(width={0}, height={1})").format(self.width, self.height))

  def set_width(self, value):
    self.width = value
  
  def set_height(self, value):
    self.height = value

  def get_area(self):
    return(self.width * self.height)
  
  def get_perimeter(self):
    return(2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return("Too big for picture.")
    else:
      return( ( ("*" * self.width)+ "\n" ) * self.height)
  
  def get_amount_inside(self, Shape):
    
    return( self.get_area() // Shape.get_area() )
    
class Square(Rectangle):
  def __init__(self, side):
    Rectangle.width = side
    Rectangle.height = side

  def set_side(self, value):
    Rectangle.set_width(self, value)
    Rectangle.set_height(self, value)

  def __str__(self):
    return(("Square(side={0})").format(self.width) )

  


