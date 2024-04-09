from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Definindo as dimensões da janela
left = -50
right = 50
bottom = -50
top = 50

# Variável para armazenar o alvo da interação do mouse
target = None

# Dicionário para armazenar as cores e suas posições
color_data = {
    "r":[127, 0],
    "g":[127, 0],
    "b":[127, 0]
}

def draw_red_slider():
    glBegin(GL_QUADS)
    glColor3ub(0,0,0)
    glVertex2d(-40,40)
    glVertex2d(-40,30)
    glColor3ub(255,0,0)
    glVertex2d(40,30)
    glVertex2d(40,40)
    glEnd()

def draw_green_slider():
    glBegin(GL_QUADS)
    glColor3ub(0,0,0)
    glVertex2d(-40,20)
    glVertex2d(-40,10)
    glColor3ub(0,255,0)
    glVertex2d(40,10)
    glVertex2d(40,20)
    glEnd()

def draw_blue_slider():
    glBegin(GL_QUADS)
    glColor3ub(0,0,0)
    glVertex2d(-40,0)
    glVertex2d(-40,-10)
    glColor3ub(0,0,255)
    glVertex2d(40,-10)
    glVertex2d(40,0)
    glEnd()

def draw_slider_bar(x, y):
    glBegin(GL_LINE_STRIP)
    glColor3ub(255,255,255)
    glVertex2d(x,y-5)
    glVertex2d(x,y+5)
    glEnd()

def draw_reset_button():
    glBegin(GL_QUADS)
    glColor3ub(100,100,100)
    glVertex2d(10,-30)
    glVertex2d(10,-20)
    glVertex2d(40,-20)
    glVertex2d(40,-30)
    glEnd()

def draw_color_square():
    glBegin(GL_QUADS)
    glColor3ub(int(color_data["r"][0]),int(color_data["g"][0]),int(color_data["b"][0]))
    glVertex2d(-40,-30)
    glVertex2d(-40,-20)
    glVertex2d(-10,-20)
    glVertex2d(-10,-30)
    glEnd()

def initialize():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(left, right, bottom, top, -1.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def render():
    glClearColor(42/255, 40/255, 37/255, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_red_slider()
    draw_slider_bar(color_data["r"][1],35)
    draw_green_slider()
    draw_slider_bar(color_data["g"][1],15)
    draw_blue_slider()
    draw_slider_bar(color_data["b"][1],-5)
    draw_reset_button()
    draw_color_square()
    glutSwapBuffers()

def mouse_button_callback(button, state, x,y):
    global target
    global color_data
    if(button == 0 and state == 0):
        coords = get_world_coords(x,y)
        if (coords[0] >= -40 and coords[0] <= 40 and coords[1] >= 30 and coords[1] <= 40):
            target = "r"
            mouse_motion_callback(x,y)
        elif (coords[0] >= -40 and coords[0] <= 40 and coords[1] >= 10 and coords[1] <= 20):
            target = "g"
            mouse_motion_callback(x,y)
        elif (coords[0] >= -40 and coords[0] <= 40 and coords[1] >= -10 and coords[1] <= 0):
            target = "b"
            mouse_motion_callback(x,y)
        elif (coords[0] >= 10 and coords[0] <= 40 and coords[1] >= -30 and coords[1] <= -20):
            color_data = {
                "r":[127, 0],
                "g":[127, 0],
                "b":[127, 0]
            }
        else: 
            target = None
    glutPostRedisplay()

def mouse_motion_callback(x,y):
    global target
    global color_data
    coords = get_world_coords(x,y)
    if(target == "r" or target == "g" or target == "b"):
        coord_temp = coords[0]+40
        if coord_temp < 0: coord_temp = 0
        if coord_temp > 80: coord_temp = 80
        color_data[target] = [coord_temp*255/80, coord_temp-40]

def get_world_coords(x, y):
    xr = right
    xl = left
    yt = top
    yb = bottom
    zn = 1.0
    zf = -1.0
    
    P =[
        [2/(xr-xl), 0.0, 0.0, -(xr+xl)/(xr-xl)],
        [0.0, 2/(yt-yb), 0.0, -(yt+yb)/(yt-yb)],
        [0.0, 0.0, -2/(zf-zn), -(zf+zn)/(zf-zn)],
        [0.0, 0.0, 0.0, 1.0],
    ]

    PM = np.array(P)

    invP = np.linalg.inv(PM)

    viewport = glGetIntegerv(GL_VIEWPORT)
    ywin = viewport[3] - y
    xndc = (2*(x-viewport[0]))/viewport[2] -1
    yndc = (2*(ywin-viewport[1]))/viewport[3] -1
    zndc = 0
    wndc = 1
    vndc = np.array([xndc, yndc, zndc,wndc])

    world = np.matmul(invP, vndc)

    return world[0], world[1]

def main():
    global wind
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("Lab 02 - Color Picker")
    glutDisplayFunc(render) 
    glutMouseFunc(mouse_button_callback)
    glutMotionFunc(mouse_motion_callback)
    initialize()
    glutMainLoop()
    
if __name__ == "__main__":
    main()
