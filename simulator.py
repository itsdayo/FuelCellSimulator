# import pygame module in this program
import pygame
import time
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pem = "images/PEMcells.png"
smallH = "images/hydrogen+.png"
smallO = "images/oxygen-2.png"
BigO = "images/oxygen2.png"
bigH = "images/hydrogen2.png"
electron = "images/electron.png"
water = "images/water.png"

pygame.init()
screen = pygame.display.set_mode((1000, 800))
background = pygame.image.load(pem).convert()
hydrogen2 = pygame.image.load(bigH).convert_alpha()
oxygen = pygame.image.load(smallO).convert_alpha()
oxygen2 = pygame.image.load(BigO).convert_alpha()
electron = pygame.image.load(electron).convert_alpha()
hydrogen = pygame.image.load(smallH).convert_alpha()
water = pygame.image.load(water).convert_alpha()



# set the pygame window name
pygame.display.set_caption("PEM Fuel Cell")


# Indicates pygame is running
run = True

# infinite loop
while run:
    # creates time delay of 10ms
    pygame.time.delay(10)

    
   
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:

            # it will make exit the while loop
            run = False
  
    

    screen.blit(background, (0, 0))
    screen.blit(hydrogen2, (170, 160))
    screen.blit(electron, (270, 519))
    screen.blit(electron, (470, 419))
    screen.blit(electron, (610, 519))
    screen.blit(oxygen, (610, 260))
    screen.blit(oxygen2, (730, 10))
    screen.blit(oxygen2, (620, 100))
    screen.blit(water, (710, 280))
    screen.blit(water, (750, 380))
    screen.blit(hydrogen, (500, 300))

    # drawing objects on screen 
    while True:
        i = 0
        while i < 100:
            screen.blit(background, (0, 0))
            position = hydrogen2.get_rect()
            position2 = hydrogen.get_rect()
            position3 = electron.get_rect()
            position4 = electron.get_rect()
            position5 = electron.get_rect()
            position6 = electron.get_rect()
            position7 = oxygen2.get_rect()
            position8 = oxygen2.get_rect()
            position9 = water.get_rect()
            position10 = water.get_rect()
            position = position.move(170-i, 160)
            position2 = position2.move(500-i, 300)
            position3 = position3.move(270, 519-i)
            position4 = position4.move(470-i, 519)
            position5 = position5.move(610, 419+i)
            position6 = position6.move(610, 260-i)
            position7 = position7.move(730, 10-i)
            position8 = position8.move(620+i, 100)
            position9 = position9.move(710-i, 280)
            position10 = position10.move(750, 380-i)
            screen.blit(hydrogen2, position)
            screen.blit(hydrogen, position2)
            screen.blit(electron, position3)
            screen.blit(electron, position4)
            screen.blit(electron, position5)
            screen.blit(oxygen, position6)
            screen.blit(oxygen2, position7)
            screen.blit(oxygen2, position8)
            screen.blit(water, position9)
            screen.blit(water, position10)
            
            pygame.display.update()
            pygame.time.delay(2)
            i+=1
            print(i)
            
            
            pygame.display.update()
            
            screen.blit(hydrogen2, (170, 160))
        if not i<100:
            break
    # it refreshes the window
        pygame.display.update()
pygame.display.update()
# closes the pygame window
pygame.quit()
