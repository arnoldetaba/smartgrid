import pygame, sys
from pygame.locals import *
import time

BLUE=(0,150,255)

def draw(color):
    pygame.init()

    DISPLAY=pygame.display.set_mode((900,400),0,32)

    BLACK=(0,0,0)
    BLUE=(0,0,255)
    YELLOW=(255,255,0)
    color = BLUE

    DISPLAY.fill(BLACK)
    pygame.display.set_caption("lamp1")
    pygame.display.flip()

    pygame.draw.rect(DISPLAY,color,(50,50,200,200))
    pygame.draw.rect(DISPLAY,color,(300,50,200,200))
    pygame.draw.rect(DISPLAY,color,(550,50,200,200))

    i = 0
    while True:
        i += 1
        print(i)
        if i == 5:
            pygame.draw.rect(DISPLAY,YELLOW,(300,50,200,200))
        time.sleep(1)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    draw(BLUE)
