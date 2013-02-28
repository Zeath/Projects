from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Image import *
from player import *
from box import *
from fireParticle import *
from house import *
from time import *

def makeMap(filename):
    global groundSide
    image = open(filename)
    
    ix = image.size[0]
    iy = image.size[1]
    image = image.tostring("raw", "RGBX", 0, -1)
    line = 0
    num = 0
        
    for i in range(ix*iy):
        #print ord(image[i*4])
        #print i
        if num == ix:
            num = 0
            line += 1
        if ord(image[i*4]) == 255:
            boxList.append(Box(Vect3(x=num*3-groundSide/2,y=line*3-groundSide/2,z=0), boxTex))

        if ord(image[i*4]) == 200:
            boxList.append(Box(Vect3(x=num*3-groundSide/2,y=line*3-groundSide/2,z=0), boxTex))
            boxList.append(Box(Vect3(x=num*3-groundSide/2,y=line*3-groundSide/2,z=3), boxTex))

            
        num += 1


        
def loadTexture(filename):
    image = open(filename)
    
    ix = image.size[0]
    iy = image.size[1]
    image = image.tostring("raw", "RGBX", 0, -1)
    
    # Create Texture	
    # There does not seem to be support for this call or the version of PyOGL I have is broken.
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)   # 2d texture (x and y size)
	
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    ##glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    return texture



def mouseMove(x,y):
        global player
        mouse_sens = 0.00666
        player.rotate(-x*mouse_sens, -y*mouse_sens)

def keyPress(key):
        global player
        if key == "e":
            boxList.append(Box(Vect3(x=player.pos.x,y=player.pos.y,z=player.pos.z), boxTex))

"""
def mousePress():
        processMouse(button,state,x,y)
            if state == GLUT_DOWN:
                fireParticleList.insert(len(fireParticleList),FireParticle(Vect3(x=player.pos.x,y=player.pos.y,z=player.pos.z), fireParticleTex))
"""

def startUp():
        global player, groundTex, boxList, houseList, fireParticleList, boxTex, groundSide, groundTexSide, fireParticleTex, dt, lastClock
        lastClock = 1.0
        dt = 1.0
        groundSide = 64*3
        groundTexSide = 64
        groundTex = loadTexture("Textures/Ground.png")
        boxTex = loadTexture("Textures/Woodbox.png")
        fireParticleTex = loadTexture("Textures/Fire.png")
        player = Player()
        boxList = []
        fireParticleList = []
        #houseList = [House(Vect3(x=0,y=12,z=0), houseTex), House(Vect3(x=0,y=27,z=0), houseTex), House(Vect3(x=15,y=12,z=0), houseTex), House(Vect3(x=15,y=27,z=0), houseTex) ]
        makeMap("Textures/Red.png")
        glEnable(GL_POLYGON_SMOOTH)
        glEnable(GL_BLEND)
        glutSetCursor(GLUT_CURSOR_NONE)

 
def collision(xSize, ySize, zSize, boxx, boxy, boxz):
        global player
        
	
	
def update(keyIsPressed):
        global player, fireParticleTex, fireParticleList, fireParticle, dt, lastClock

        dt = 100.0 * (clock() - lastClock)
        lastClock = clock()
        
        if keyIsPressed[ord("w")]:
            player.stepForward(0.003,dt)
        if keyIsPressed[ord("s")]:
            player.stepForward(-0.003,dt)
        if keyIsPressed[ord("a")]:
            player.stepRight(-0.003,dt)
        if keyIsPressed[ord("d")]:
            player.stepRight(0.003,dt)
        if keyIsPressed[ord(" ")]:
            player.jump()
        if keyIsPressed[ord("q")]:
            #if int(random()*2) == 1:
            fireParticleList.append(FireParticle(Vect3(x=player.pos.x,y=player.pos.y,z=player.pos.z), fireParticleTex, player.lookDir))
            player.addForce(player.lookDir / -1.5)
        #if keyIsPressed[ord("SHIFT")]:
        #   player.jump()


        player.update(dt)
        for i in range(len(fireParticleList)):
            fireParticleList[i].update(dt)
        fireParticleList = [i for i in fireParticleList if i.exist]


def draw():
	global player, groundTex, boxList, groundSide, groundTexSide, fireParticleList, fireParticle
	
        player.setCamera()
        glLoadIdentity()
        
        for i in range(len(boxList)):
            boxList[i].draw()

        
	glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, groundTex)
        glBegin(GL_QUADS)
        
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-groundSide/2, -groundSide/2,  0.0)
        
	glTexCoord2f(groundTexSide, 0.0)
	glVertex3f(groundSide/2, -groundSide/2,  0.0)
	
	glTexCoord2f(groundTexSide, groundTexSide)
	glVertex3f(groundSide/2,  groundSide/2,  0.0)
	
	glTexCoord2f(0.0, groundTexSide)
	glVertex3f(-groundSide/2,  groundSide/2,  0.0)
	
	glEnd()
	
        glDepthMask(GL_FALSE)

	for i in range(len(fireParticleList)):
            fireParticleList[i].draw(player.strafeRDir, player.upDir)
            
        glDepthMask(GL_TRUE)











