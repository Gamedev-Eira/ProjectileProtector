#libary imports
from tkinter.tix import INCREASING
import pygame
pygame.init()

CLOCK = pygame.time.Clock() #initalises the clock to set the FPS of the program

SCREEN_SIZE = (750, 500)                        #sets a variable to hold the screen size
SCREEN = pygame.display.set_mode(SCREEN_SIZE)   #sets the screen size to the previous variable

pygame.display.set_caption("Projectile Protector V1.0") #sets window title

playGame = bool(True)   #PlayGame is a boolean variable that will allow the main game loop to run

#colour declorations
COLOUR_WHITE = (255, 255, 255)
COLOUR_BLACK = (0, 0, 0)

#variable initalisation
INCREMENT = int(25)
planeXcoord = int(0)
planeSize = [100, 50]
moveRight = bool(True)

#main game loop
while playGame:
    CLOCK.tick(10)  #sets the FPS of the program to 30
    CLOCK.tick()    #causes a game tick

    SCREEN.fill(COLOUR_WHITE)

    if(moveRight == True):
        planeXcoord = planeXcoord + INCREMENT;
        if (planeXcoord == SCREEN_SIZE[0] - (INCREMENT + planeSize[0]) ):
            moveRight = False

    elif (moveRight == False):
        planeXcoord = planeXcoord - INCREMENT;
        if (planeXcoord == (0 + INCREMENT)):
            moveRight = True
        
    pygame.draw.rect(SCREEN, COLOUR_BLACK, pygame.Rect(planeXcoord, INCREMENT, planeSize[0], planeSize[1]))

    pygame.display.flip()

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:   #checks for the user clicking the X button, and ending the program if they do
              playGame = False          #it does this by setting playGame to false, ending the condition for the previous while to run

pygame.quit()                           #now the user is out of the loop, this code makes the game end