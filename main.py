from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import numpy as np

from circle import *
from border import *
from mid_point_lines import *
from checkobstacle import *

def showScreen():

    pygame.init()                 # Initialize pygame

    display = (750, 500)
    # Set display wtih OpenGL
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(0, 750, 500, 0, -1, 1)

    radius = 25
    x = 10
    y = 0

    font = pygame.font.Font('freesansbold.ttf', 23)
    
    def drawText():#start and goal text
        textSurface1 = font.render(
            'Start', True, (255, 255, 255, 255), (0, 0, 0, 0))
        textData1 = pygame.image.tostring(textSurface1, "RGBA", True)
        glWindowPos2d(75, 450)
        glDrawPixels(textSurface1.get_width(), textSurface1.get_height(),
                     GL_RGBA, GL_UNSIGNED_BYTE, textData1)

        textSurface2 = font.render(
            'Goal', True, (255, 255, 255, 255), (0, 0, 0, 0))
        textData2 = pygame.image.tostring(textSurface2, "RGBA", True)
        glWindowPos2d(680, 150)
        glDrawPixels(textSurface2.get_width(), textSurface2.get_height(),
                     GL_RGBA, GL_UNSIGNED_BYTE, textData2)

        textSurface3 = font.render(
            'Score =', True, (255, 255, 255, 255), (0, 0, 0, 0))
        textData3 = pygame.image.tostring(textSurface3, "RGBA", True)
        glWindowPos2d(20, 50)
        glDrawPixels(textSurface3.get_width(), textSurface3.get_height(),
                     GL_RGBA, GL_UNSIGNED_BYTE, textData3)

    
    def drawText2():#winnertext
        font2 =  pygame.font.Font('freesansbold.ttf', 34)
        textSurface1 = font2.render(
            'Winner', True, (255, 255, 255, 255), (0, 0, 0, 0))
        textData1 = pygame.image.tostring(textSurface1, "RGBA", True)
        glWindowPos2d(300, 20)
        glDrawPixels(textSurface1.get_width(), textSurface1.get_height(),
                     GL_RGBA, GL_UNSIGNED_BYTE, textData1)                                          

    status = True
    while status:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  
                    x -= 25
                elif event.key == pygame.K_RIGHT:  
                    x += 25
                elif event.key == pygame.K_UP:  
                    y -= 25
                elif event.key == pygame.K_DOWN:  
                    y += 25

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #
        if x > 750 - radius:            # Boundaries of the character movement
            x = 750 - radius

        if x < 0 + radius+10:
            x = 0 + radius+25

        if y > 500 - radius-10:
            y = 500 - radius-25

        if y < 0 + radius+10:
            y = 0 + radius+25

        obstacles()# drawing the boundaries
        
        x,y=check(x,y,radius)#checking the obstacles
        drawCurve(radius,x, y)       # Draw the character
        drawlines()
        drawText()
        if x == 700 and y == 350: #checking winner position
            drawText2()
        pygame.display.flip()  # Update the full display Surface to the screen
       # pygame.time.wait(10)  # pause the program for an amount of time


showScreen()
