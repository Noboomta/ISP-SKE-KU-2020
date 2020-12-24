"""
Perform these refactorings:

1. Replace Array With Object

   Define a Point class with (x,y) values instead of using a tuple 
   with 2 elements for x,y values.
   Access the attributes of a Point directly instead of using "get" methods.
   Its faster and more readable.  
   Modify the code to use points for x,y values.
   Write the Point class in this file (before the functions).

   > You need the change the code in __main__ to use Points, too.

2. Extract Method & Move Method

   Extract the code that computes distance between 2 points.
   Define a "distance_to(Point)" method in Point class to compute that.

3. Use the API to make code more readable

   Python 'math' module has a function that computes Euclidean distance,
   so you don't need to write sqrt(a**2 + b**2).
   Use that function in your code. It makes the code simpler.

   Type help(math) in Python to find this function.

4. Inline Temp Variables

   After the above refactorings, the code for perimeter is so simple
   that the temp variables p and q aren't helpful any more.
   Apply "Inline Temp Variable".

5. Extract Method and encapsulate it.

   show_points formats each point as a string like "(3,4)".
   The Point class should provide the string form itself.
   In Point, write the standard Python method for returning 
   a string form of an object.

   When you are done, no code in perimeter or show_points
   accesses the attributes of a Point (good encapsulation).

6. Eliminate Duplicate Code.  There is some duplicate code in main.
   Remove duplicate code by defining a method and using it.

   When you done, main will not contain any "print" statements.

"""
import math

class Point:
   """Class Point to store the parameter x and y."""

   def __init__(self, x, y):
      self.x = x
      self.y = y
   
   def distance_to(self, point):
      """Class method to return the distance 2 Point."""
      distance = math.hypot((self.x - point.x), (self.y - point.y))
      return distance

   def __str__(self):
      return f"({self.x},{self.y})"

   @classmethod
   def perimeter(cls, *points):
      """Class method to return the perimeter of all Point."""
      if len(points) < 2:
        raise ValueError("Must specify at least 2 points.")
      perimeter = 0
      for k in range(0, len(points)):
         perimeter += points[k].distance_to(points[k-1])
      return perimeter

def print_ans(msg, *p):
   print(msg, *p)

if __name__ == '__main__':
    """Print some simple polygons and their perimeters."""

    # TODO: after refactoring #1 change the tuples to a Point object.

   #  print("Right triangle with corners", Point(0,0), Point(3,0), Point(0,4))
    print_ans("Right triangle with corners", (Point(0,0), Point(3,0), Point(0,4)))
   #  print("perimeter = ", Point.perimeter(Point(0,0), Point(3,0), Point(0,4)))
    print_ans("perimeter = ", Point.perimeter(Point(0,0), Point(3,0), Point(0,4)))

    # After refactoring use: points = Point(0,0), ...
    points = Point(0,0), Point(3,0), Point(3,5), Point(0,5)
   #  print("Rectangle with corners", (*points))
    print_ans("Rectangle with corners", (*points))
   #  print("perimeter = ", Point.perimeter(*points))
    print_ans("perimeter = ", Point.perimeter(*points))

    # perimeter(*points) passes the elements of points as separate arguments
    # instead of a single argument, e.g. perimeter(points).

    points = Point(-2,0), Point(2,0), Point(2,4), Point(0,6), Point(-2,4)
   #  print("Pentagon shaped like a house", (*points))
    print_ans("Pentagon shaped like a house", (*points))
   #  print("perimeter = ", Point.perimeter(*points))
    print_ans("perimeter = ", Point.perimeter(*points))
