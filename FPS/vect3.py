from random import *
from math import *

class Vect3:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def copy(self):
        return Vect3(x=self.x, y=self.y, z=self.z)

    def __add__(self, other):
        result = Vect3()
        result.x = self.x + other.x
        result.y = self.y + other.y
        result.z = self.z + other.z
        return result

    def __mul__(self, other):
        result = Vect3()
        result.x = self.x * other
        result.y = self.y * other
        result.z = self.z * other
        return result

    def __sub__(self, other):
        result = Vect3()
        result.x = self.x - other.x
        result.y = self.y - other.y
        result.z = self.z - other.z
        return result
    
    def __neg__(self):
        result = Vect3()
        result.x = -self.x
        result.y = -self.y
        result.z = -self.z
        return result

    def norm(self):
        return sqrt(self.x**2+self.y**2+self.z**2)
        
    def __div__(self, other):
        result = Vect3()
        result.x = self.x / other
        result.y = self.y / other
        result.z = self.z / other
        return result

        

def cross(a, b):
    return Vect3(a.y*b.z-a.z*b.y, a.z*b.x-a.x*b.z, a.x*b.y-a.y*b.x)
        
def randomizeVector(a, b):
    return Vect3(a.x+((random()-0.5)*b), a.y+((random()-0.5)*b), a.z+((random()-0.5)*b))





                 
