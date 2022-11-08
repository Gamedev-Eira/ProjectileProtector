#libary imports
import pygame
pygame.init()

CLOCK = pygame.time.Clock() #initalises the clock to set the FPS of the program

SCREEN_SIZE = (700, 500)                        #sets a variable to hold the screen size
SCREEN = pygame.display.set_mode(SCREEN_SIZE)   #sets the screen size to the previous variable

pygame.display.set_caption("Projectile Protector V0.0") #sets window title

playGame = bool(True)   #PlayGame is a boolean variable that will allow the main game loop to run

#colour declorations
COLOUR_WHITE = (255, 255, 255)
COLOUR_BLACK = (0, 0, 0)

#main game loop
while playGame:
    CLOCK.tick(60)  #sets the FPS of the program to 60
    CLOCK.tick()    #causes a game tick

    SCREEN.fill(COLOUR_WHITE)
    pygame.display.flip()

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:   #checks for the user clicking the X button, and ending the program if they do
              playGame = False          #it does this by setting playGame to false, ending the condition for the previous while to run

pygame.quit()                           #now the user is out of the loop, this code makes the game end