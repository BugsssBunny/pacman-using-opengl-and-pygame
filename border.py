from OpenGL.GL import *


def obstacles():
    x_max = 750
    y_max = 500
    min = 0
    border = 10
    glColor3f(0.5, 0.3, 0.5)
    glBegin(GL_QUADS)
   #upper
    #Boundaries
    glVertex2f(min, min)
    glVertex2f(x_max, min)
    glVertex2f(x_max, border)
    glVertex2f(min, border)
  # left
    glVertex2f(min, min)
    glVertex2f(min, y_max)
    glVertex2f(border, y_max)
    glVertex2f(border, min)
   # down
    glVertex2f(min, y_max)
    glVertex2f(x_max, y_max)
    glVertex2f(x_max, y_max - border)
    glVertex2f(min, y_max - border)
#right
    glVertex2f(x_max, y_max)
    glVertex2f(x_max, min)
    glVertex2f(x_max - border, min)
    glVertex2f(x_max - border, y_max)

    #Obstacles

    glEnd()
