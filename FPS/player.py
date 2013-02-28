from vect3 import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from copy import copy
import math

class Player:
	def __init__(self):
                self.h8 = 1.7
                self.w8 = 80.0
		self.pos = Vect3()
		self.__dirx = 0.0
		self.__diry = 0.0
		self.lookDir = Vect3()
		self.lookDir.x = 1.0
		self.walkDir = Vect3()
		self.walkDir.x = 1.0
		self.strafeRDir = Vect3()
		self.strafeRDir.x = 1.0
		self.upDir = cross(self.strafeRDir, self.lookDir)
		self.zSpeed = 0
		self.speed = Vect3()
		self.fF = Vect3()
		self.acc = Vect3()
	def setCamera(self):
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(65.0, 16.0/9.0, 0.03, 200.0)#TODO send in real ratio here (not 16.0/9.0)
                camPos = copy(self.pos)
                camPos.z += self.h8
		at = camPos + self.lookDir
		gluLookAt(camPos.x, camPos.y, camPos.z, at.x, at.y, at.z, 0, 0, 1) 
		glMatrixMode(GL_MODELVIEW)
        
        def rotate(self, incx, incy):
                eps = 0.000001
                self.__dirx += incx
                self.__diry += incy
                if self.__diry < -math.pi/2 + eps:
                        self.__diry = -math.pi/2 + eps
                if self.__diry > math.pi/2 - eps:
                        self.__diry = math.pi/2 - eps
                if self.__dirx > math.pi*2:
                        self.__dirx += -math.pi*2
                if self.__dirx < -math.pi*2:
                        self.__dirx += math.pi*2
                self.lookDir.x = math.cos(self.__dirx)*math.cos(self.__diry)
                self.lookDir.y = math.sin(self.__dirx)*math.cos(self.__diry)
                self.lookDir.z = math.sin(self.__diry)

                self.walkDir.x = math.cos(self.__dirx)
                self.walkDir.y = math.sin(self.__dirx)
                self.walkDir.z = 0

                self.strafeRDir.x = math.cos(self.__dirx-math.pi/2)
                self.strafeRDir.y = math.sin(self.__dirx-math.pi/2)
                self.strafeRDir.z = 0

                self.upDir = cross(self.strafeRDir, self.lookDir)
                
        def stepForward(self,stepLength,dt):
                self.speed += (self.walkDir * stepLength) * dt

        def stepRight(self,stepLength,dt):
                self.speed += (self.strafeRDir * stepLength) * dt

        def jump(self):
                if self.pos.z <= 0.5:
                        self.addForce(Vect3(z=0.05 * self.w8))

        def update(self,dt):
                
                if self.pos.z < 0.0001:
                        self.pos.z = 0.0
                        self.fF = -self.speed / (self.speed.norm()+1) * 3.0
                else:
                        self.fF = Vect3()
                        self.addForce(Vect3(z=-0.005 * self.w8))

                self.addForce(self.fF)
                
                self.pos += self.speed * dt
                self.speed += self.acc * dt
                self.acc = Vect3()

                



        def addForce(self, f):
                self.acc += f / self.w8








                

