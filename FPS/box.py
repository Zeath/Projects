from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Image import *
from vect3 import *
from fps import *
        


class Box:
    def __init__(self, position, myTex):
        self.pos = position.copy()
        self.length = 3.0
        self.boxTexSide = 1.0
        self.myTexture = myTex

    def draw(self):
        glPushMatrix()
        glTranslatef(self.pos.x, self.pos.y, self.pos.z)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.myTexture)
        glBegin(GL_QUADS)
###       
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-self.length/2, -self.length/2,  0.0)
        
	glTexCoord2f(self.boxTexSide, 0.0)
	glVertex3f(self.length/2, -self.length/2,  0.0)
	
	glTexCoord2f(self.boxTexSide, self.boxTexSide)
	glVertex3f(self.length/2,  -self.length/2,  self.length)
	
	glTexCoord2f(0.0, self.boxTexSide)
	glVertex3f(-self.length/2,  -self.length/2,  self.length)
###
	glTexCoord2f(0.0, 0.0)
        glVertex3f(-self.length/2, self.length/2,  0.0)
        
	glTexCoord2f(self.boxTexSide, 0.0)
	glVertex3f(-self.length/2, -self.length/2,  0.0)
	
	glTexCoord2f(self.boxTexSide, self.boxTexSide)
	glVertex3f(-self.length/2,  -self.length/2,  self.length)
	
	glTexCoord2f(0.0, self.boxTexSide)
	glVertex3f(-self.length/2,  self.length/2,  self.length)
###
	glTexCoord2f(0.0, 0.0)
        glVertex3f(self.length/2, self.length/2,  0.0)
        
	glTexCoord2f(self.boxTexSide, 0.0)
	glVertex3f(-self.length/2, self.length/2,  0.0)
	
	glTexCoord2f(self.boxTexSide, self.boxTexSide)
	glVertex3f(-self.length/2,  self.length/2,  self.length)
	
	glTexCoord2f(0.0, self.boxTexSide)
	glVertex3f(self.length/2,  self.length/2,  self.length)
###
	glTexCoord2f(0.0, 0.0)
        glVertex3f(self.length/2, -self.length/2,  0.0)
        
	glTexCoord2f(self.boxTexSide, 0.0)
	glVertex3f(self.length/2, self.length/2,  0.0)
	
	glTexCoord2f(self.boxTexSide, self.boxTexSide)
	glVertex3f(self.length/2,  self.length/2,  self.length)
	
	glTexCoord2f(0.0, self.boxTexSide)
	glVertex3f(self.length/2,  -self.length/2,  self.length)
###
	glTexCoord2f(0.0, 0.0)
        glVertex3f(-self.length/2, -self.length/2,  self.length)
        
	glTexCoord2f(self.boxTexSide, 0.0)
	glVertex3f(self.length/2, -self.length/2,  self.length)
	
	glTexCoord2f(self.boxTexSide, self.boxTexSide)
	glVertex3f(self.length/2,  self.length/2,  self.length)
	
	glTexCoord2f(0.0, self.boxTexSide)
	glVertex3f(-self.length/2,  self.length/2,  self.length)
###
	glTexCoord2f(0.0, 0.0)
        glVertex3f(-self.length/2, -self.length/2,  0)
        
	glTexCoord2f(self.boxTexSide, 0.0)
	glVertex3f(self.length/2, -self.length/2,  0)
	
	glTexCoord2f(self.boxTexSide, self.boxTexSide)
	glVertex3f(self.length/2,  self.length/2,  0)
	
	glTexCoord2f(0.0, self.boxTexSide)
	glVertex3f(-self.length/2,  self.length/2,  0)


	glEnd()
        glPopMatrix()
