#libary imports
from tkinter.tix import INCREASING
import pygame
import math
pygame.init()

CLOCK = pygame.time.Clock() #initalises the clock to set the FPS of the program

SCREEN_SIZE = (725, 550)                        #sets a variable to hold the screen size
SCREEN = pygame.display.set_mode(SCREEN_SIZE)   #sets the screen size to the previous variable

pygame.display.set_caption("Projectile Protector V1.1") #sets window title

playGame = bool(True)   #PlayGame is a boolean variable that will allow the main game loop to run

#colour declorations
COLOUR_WHITE = (255, 255, 255)
COLOUR_BLACK = (0, 0, 0)
COLOUR_GREEN = (0, 255, 25)

#variable initalisation
INCREMENT = int(25)

#class initalisation
class Plane():
    
    def __init__(self):
        self.moveRight = bool(True)
        self.planeHitbox = pygame.Rect(INCREMENT, INCREMENT, 100, 50)

    def movePlane(self):
        if(self.moveRight == True):
            self.planeHitbox.move_ip(INCREMENT/5, 0)

            if(self.planeHitbox.right >= (SCREEN_SIZE[0] - INCREMENT)):
                self.moveRight = False

        elif(self.moveRight == False):
            self.planeHitbox.move_ip(-INCREMENT/5, 0)

            if(self.planeHitbox.left <= INCREMENT):
                self.moveRight = True

    def drawPlane(self):
        #updates the x coordinate of planeHitbox after it's been updated by movePlane()
        pygame.draw.rect(SCREEN, COLOUR_BLACK, self.planeHitbox)   #draws the rectangle on the screen with the updated position

class House():
    
    def __init__(self, groundHeight, houseNumber):
        self.houseOffset = int(1)
        self.listOfHouses = []
        self.numOfHouses = int(houseNumber)

        for x in range(self.numOfHouses):
            temp = pygame.Rect((INCREMENT*self.houseOffset) + (75*(self.houseOffset-1)), (groundHeight-50), 75, 50)
            self.listOfHouses.append(temp)
            self.houseOffset += 1

    def showHouseCenter(self, houseAccess):
        return self.listOfHouses[houseAccess].center

    def drawHouse(self):
        #updates the x coordinate of planeHitbox after it's been updated by movePlane()
        for x in range(self.numOfHouses):
            pygame.draw.rect(SCREEN, COLOUR_BLACK, self.listOfHouses[x])  

class Misile():

    def __init__(self, start, end, size):
        #first bracket is difference between starting point and the end point on the x coordinate
        #second bracket is the difference between the end point and the start point on the y coordinate
        #the latter is divided from the former to calculate the amount the missile needs to move on the X axis
        self.moveX = (end[1] - start[1]) / (end[0] - start[0])
        self.misileHitbox = pygame.Rect(start[0], start[1], size, size)

        print(self.moveX)

    def moveMisile(self):
        pygame.Rect.move_ip(self.misileHitbox, self.moveX, 5)
        pygame.draw.rect(SCREEN, COLOUR_BLACK, self.misileHitbox)

#main game loop
if playGame == True:
    
    groundHeight = int(SCREEN_SIZE[1] - (INCREMENT*2))
    houseNumber = int(7)

    plane = Plane()    #initalises the object plane
    houses = House(groundHeight, houseNumber)  #initalise houses
    missile = Misile([25, 75], [100, 475], 5)


    while(playGame == True):
        CLOCK.tick(30)  #sets the FPS of the program to 30
        CLOCK.tick()    #causes a game tick

        SCREEN.fill(COLOUR_WHITE)   #make screen colour white

        #groundRect = pygame.Rect()

        pygame.draw.rect(SCREEN, COLOUR_GREEN, (0, groundHeight, SCREEN_SIZE[0], SCREEN_SIZE[1]))

        plane.movePlane()   #calls code to move the plane
        plane.drawPlane()   #draws the plane's updated position

        houses.drawHouse()

        missile.moveMisile()

        pygame.display.flip()   #updates screen

        for event in pygame.event.get():    #checks for the user clicking the X button, and ending the program if they do
            if event.type == pygame.QUIT:   #it does this by setting playGame to false, ending the condition for the previous while to run
                playGame = False          

    pygame.quit()                           #now the user is out of the loop, this code makes the game end
