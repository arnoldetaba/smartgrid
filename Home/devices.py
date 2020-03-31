from random import randint
import pygame, sys
from pygame.locals import *

class ElectricLamp():
    # Lamp should be created in on state by default.
    def __init__(self, Id, min_consume, max_consume):
        self.state = True
        self.min_consumption = min_consume
        self.max_consumption = max_consume
        self.id = Id


    def kill(self):
        # lamp is effectively killed
        self.state = False
        # hide rectangle
        BLACK = (0, 0, 0)
        if self.state == False:
            return False
    def up(self):
        # lamp is set back on by owner
        self.state = True
        print("up called")
        BLUE = (0, 0, 255)
        if self.state == True:
            return True
    def emit(self):
        if self.state == True:
            # lamp is on and consumes energy
            return randint(
                    self.min_consumption,
                    self.max_consumption
                    )
        else:
            # lamp is off and doesnot consume energy
            return 0
    def __str__(self):
        return self.id

    def draw(self):
        pygame.init()

        DISPLAY=pygame.display.set_mode((300,300),0,32)

        WHITE=(255,255,255)
        BLUE=(0,0,255)

        DISPLAY.fill(WHITE)
        while True:
            if self.state == True:
                pygame.draw.rect(DISPLAY,BLUE,(50,50,200,200))
            if self.state == False:
                pygame.draw.rect(DISPLAY,WHITE,(50,50,200,200))
            while True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()
