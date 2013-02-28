from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys 
import fps

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
    glClearColor(0.0,0.0,0.0, 0.0)                #0-191-255,30-144-255	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
    glutIgnoreKeyRepeat(1)	
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()					# Reset The Projection Matrix									# Calculate The Aspect Ratio Of The Window
    gluPerspective(65.0, float(Width)/float(Height), 0.03, 0.0)

    glMatrixMode(GL_MODELVIEW)



# The main drawing function. 
def DrawGLScene():
    global keyIsPressed
    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Reset The View 
    # Draw a square (quadrilateral)
    fps.update(keyIsPressed)
    fps.draw()
    #  since this is double buffered, swap the buffers to display what just got drawn. 
    glutSwapBuffers()



def keyPressed(key,x,y):
    global keyIsPressed
    if key == ESCAPE:
	    glutLeaveGameMode()
	    sys.exit()

    keyIsPressed[ord(key)] = True
    fps.keyPress(key)
    
def keyReleased(key,x,y):
    keyIsPressed[ord(key)] = False
    
def mouseMove(x,y):
	global width,  height
	middlex = width/2
	middley = height/2
	fps.mouseMove(x - middlex, y - middley) 
	if x!=middlex or y!=middley:
		glutWarpPointer(middlex, middley)


def main():
	global width,  height, keyIsPressed
	keyIsPressed = [False for i in range(0,256)]
	width = 1920
	height = 1080
	# For now we just pass glutInit one empty argument. I wasn't sure what should or could be passed in (tuple, list, ...)
	# Once I find out the right stuff based on reading the PyOpenGL source, I'll address this.
	glutInit(())

	# Select type of Display mode:   
	#  Double buffer 
	#  RGBA color
	# Alpha components supported 
	# Depth buffer
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	
	# get a 640 x 480 window 
	"""glutInitWindowSize(640, 480)
	
	# the window starts at the upper left corner of the screen 
	glutInitWindowPosition(0, 0)
	
	# Okay, like the C version we retain the window id to use when closing, but for those of you new
	# to Python (like myself), remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
	window = glutCreateWindow("Eric's fps'ish")"""
	glutGameModeString(str(width)+'x'+str(height)+':32');
	if glutGameModeGet(GLUT_GAME_MODE_POSSIBLE): 
		glutEnterGameMode()
	else:
		print("Can't play in Faullscreen mode")
		glutLeaveGameMode()
		sys.exit()
   	# Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
	# set the function pointer and invoke a function to actually register the callback, otherwise it
	# would be very much like the C version of the code.	
	glutDisplayFunc (DrawGLScene)
	
	# Uncomment this line to get full screen.
	#glutFullScreen()

	# When we are doing nothing, redraw the scene.
	glutIdleFunc(DrawGLScene)

	
	# Register the function called when the keyboard is pressed.  
	glutKeyboardFunc(keyPressed)
	glutKeyboardUpFunc(keyReleased)
	glutPassiveMotionFunc(mouseMove)
	glutMotionFunc(mouseMove)
	#glutMouseFunc(processMouse)
	# Initialize our window. 
	InitGL(width, height)

	# Start Event Processing Engine
	fps.startUp()
	glutMainLoop()


main()
