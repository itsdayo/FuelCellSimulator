# import pygame module in this program
import pygame

pem = "images/PEMcells.png"

smallH = "images/hydrogen+.png"
smallO = "images/oxygen-2.png"
BigO = "images/oxygen2.png"
bigH = "images/hydrogen2.png"
electron = "images/electron.png"
water = "images/water.png"
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
screen = pygame.display.set_mode((1000, 800))
background = pygame.image.load(pem).convert()
hydrogen2 = pygame.image.load(bigH).convert_alpha()
oxygen = pygame.image.load(smallO).convert_alpha()
oxygen2 = pygame.image.load(BigO).convert_alpha()
electron = pygame.image.load(electron).convert_alpha()
hydrogen = pygame.image.load(smallH).convert_alpha()
water = pygame.image.load(water).convert_alpha()

# create the display surface object
# of specific dimension..e(500, 500).


# set the pygame window name
pygame.display.set_caption("Moving rectangle")

# object current co-ordinates
x = 200
y = 200

# dimensions of the object
width = 20
height = 20

# velocity / speed of movement
vel = 10

# Indicates pygame is running
run = True

# infinite loop
while run:
    # creates time delay of 10ms
    pygame.time.delay(10)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:

            # it will make exit the while loop
            run = False
    # stores keys pressed
    keys = pygame.key.get_pressed()

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x > 0:

        # decrement in x co-ordinate
        x -= vel

    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < 500-width:

        # increment in x co-ordinate
        x += vel

    # if left arrow key is pressed
    if keys[pygame.K_UP] and y > 0:

        # decrement in y co-ordinate
        y -= vel

    # if left arrow key is pressed
    if keys[pygame.K_DOWN] and y < 500-height:
        # increment in y co-ordinate
        y += vel

    # completely fill the surface object
    # with black colour
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

    # drawing object on screen which is rectangle here
   
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))

    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()
