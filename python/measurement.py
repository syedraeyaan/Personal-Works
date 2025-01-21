# Module containing all the functions to compute the physical parameters of 3D and 2D shape
import math

pi = math.pi

# Circle Functions

def circle_area(r: float):
    return pi*(r**2)

def circumference(r:float):
    return 2*pi*r

def diameter(r:float):
    return 2*r

# Quadrilateral Functions

def area_straightQuad(l:float, w:float):
    return l*w

def perimeter_straightQuad(l:float, w:float):
    return 2*(l+w)

# Triangle functions

def triangle_area(s1:float, s2:float, s3:float):
   if s1 + s2 > s3 and s2 + s3 > s1: 
    
    semi = (s1+s2+s3)/3
    return math.sqrt(semi*(semi-s1)*(semi-s2)*(semi-s3))
   
   else:
    return "Invalid Triangle"

def triangle_perimeter(s1:float, s2:float, s3:float):
     if s1 + s2 > s3 and s2 + s3 > s1: 
       return s1 + s2 +s3
     else:
       return "Invalid Triangle"

def height_triangle (s1:float, s2:float, base:float):
     if s1 + s2 > base and s2 + base > s1: 
       return triangle_area(s1,s2,base)/(0.5*base)
     else:
       return "Invalid Triangle"