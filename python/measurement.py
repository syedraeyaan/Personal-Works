# Module containing all the functions to compute the physical parameters of 3D and 2D shape
import math

pi = math.pi

def circle_area(r: float):
    return pi*(r**2)

def circumference(r:float):
    return 2*pi*r

def diameter(r:float):
    return 2*r

def area_straightQuad(l:float, w:float):
    return l*w

def perimeter_straightQuad(l:float, w:float):
    return 2*(l+w)

