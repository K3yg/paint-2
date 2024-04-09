from OpenGL.GL	 import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *
import numpy as np

area = 30

def init():
    glViewport(0,0,500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-area, area, -area, area, -area, area)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
def desenhaEixos():
    glBegin(GL_LINES)
    # Eixo X
    glVertex2f(20,0)
    glVertex2f(-20,0)
    # Eixo Y
    glVertex2f(0,20)
    glVertex2f(0,-20)
    glEnd()

def desenhaCirculo(r, px=0,py=0):
    x = np.pi/18    
    
    glBegin(GL_LINE_LOOP)

    for i in range(36):
        a = i * x
        glVertex2f(px + (r * np.cos(a)), py +(r * np.sin(a)))       

    glEnd()

def desenhaEspiral(r):
    x = np.pi/18
    
    glBegin(GL_LINE_STRIP)

    for i in range(100):
        a = i * x
        glVertex2f((r*i * np.cos(a)),(r*i * np.sin(a)))       

    glEnd()

def desenhaTriangulo():
    glBegin(GL_LINE_LOOP)
    glVertex3f(0,-5,0)
    glVertex3f(-5,5,0)
    glVertex3f(5,5,0)
    glEnd()

def desenhaForma():
    desenhaCirculo(5,-5,5)
    desenhaCirculo(5,5,5)
    desenhaCirculo(5,0,-5)
    desenhaTriangulo()

def pegarTecla(t,x,y):
    global area
    key = str(t, encoding='utf-8')
    if (key == 'a'):
        area += 1
    elif (key == 'd' and area > 1):
        area -= 1


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1,1,1)
    glClearColor(0,0,0, 1)

    desenhaEixos()

    # Questão 1
    # desenhaCirculo(5)

    # Questão 2
    # Utilizando a tecla 'a' e 'd', para afastar e aproximar o zoom, respectivamente.

    # Questão 3
    # desenhaEspiral(.1)

    # Questão 4
    # desenhaForma()
    
    init()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitWindowSize(500,500)
    glutInitWindowPosition(700,200)
    window = glutCreateWindow("Teste - CG")
    # Questão 2
    # ==========================
    glutKeyboardFunc(pegarTecla)
    # ==========================
    glutIdleFunc(showScreen)
    glutDisplayFunc(showScreen)
    glutMainLoop()

if __name__ == "__main__":
    main()