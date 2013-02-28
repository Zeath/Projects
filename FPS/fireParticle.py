from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import *
from Image import *
from vect3 import *
from fps import *
        


class FireParticle:
    def __init__(self, position, myTex, speed):
        self.pos = position.copy()
        self.length = random()+0.5
        self.fireTexSide = 1.0
        self.myTexture = myTex
        self.speed = randomizeVector(speed, 0.4) * (random() / 10 + 0.15)
        self.exist = True
    

    def update(self, dt):
        self.pos += self.speed
        self.speed = self.speed * 0.995
        self.length = self.length * 1.0035
        self.pos.z += 0.01
        if self.length > 3.5:
            self.exist = False
        if self.pos.z < 0.1:
            self.pos.z = 0.1
        
           
        
        
    def draw(self, right, up):
        glPushMatrix()
        glTranslatef(self.pos.x, self.pos.y, self.pos.z)
        glEnable(GL_TEXTURE_2D)
        glEnable (GL_BLEND)
        glBlendFunc (GL_ONE,GL_ONE)
        glBindTexture(GL_TEXTURE_2D, self.myTexture)
        glBegin(GL_QUADS)
###       
        glTexCoord2f(0.0, 0.0)
        glVertex3f(self.length*(-right.x-up.x), self.length*(-right.y-up.y), self.length*(-up.z))
        
	glTexCoord2f(self.fireTexSide, 0.0)
	glVertex3f(self.length*(right.x-up.x), self.length*(right.y-up.y), self.length*(-up.z))
	
	glTexCoord2f(self.fireTexSide, self.fireTexSide)
	glVertex3f(self.length*(right.x+up.x), self.length*(right.y+up.y), self.length*(up.z))
	
	glTexCoord2f(0.0, self.fireTexSide)
	glVertex3f(self.length*(-right.x+up.x), self.length*(-right.y+up.y), self.length*(up.z))

	glEnd()
	glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glPopMatrix()
