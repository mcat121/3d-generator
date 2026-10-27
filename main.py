import pygame
import time
import random
import square # type: ignore
import file_load # type: ignore


# veriable intitlize
space = True
yp = 0
xp = 0
randX1 = 0
randX2 = 0
randX3 = 0
randX4 = 0
randY1 = 0
randY2 = 0
randY3 = 0
randY4 = 0
dense = 0
colorr = 20
colorg = 100
colorb = 250
# veriable configs
#screen
res_X = 1280
res_Y = 720
running = True

#loads objs?
file_load.obj_read("/home/mastercat/Documents/GitHub/3d-generator/Part Studio 1 - Part 1.obj")
print("~~~~~~~~~~")



# start shit
screen = pygame.display.set_mode((res_X, res_Y))
surface = screen


class Block(pygame.sprite.Sprite):
    

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

block = Block((255, 0, 0), 50, 25)
block.rect.topleft = (-1, -1)


while running:
    for event  in pygame.event.get():
        # quit when closed :3
        if event.type == pygame.QUIT:
            running = False

    

    # detects keyboard shit i think (im kinda slow)
    keys = pygame.key.get_pressed()


    # screen drawing
    # math test
       
    if keys[pygame.K_SPACE]:
        if space or [pygame.K_BACKSPACE]:
            #test line
            time.sleep(0.1)
            randX1 = random.randint(0, res_X) 
            randX2 = random.randint(0, res_X) 
            randY1 = random.randint(0, res_Y) 
            randY2 = random.randint(0, res_Y) 
            randX3 = random.randint(0, res_X) 
            randX4 = random.randint(0, res_X) 
            randY3 = random.randint(0, res_Y) 
            randY4 = random.randint(0, res_Y) 
            dense = 10000
            colorr = random.randint(0, 255) 
            colorg = random.randint(0, 255) 
            colorb = random.randint(0, 255) 
            
            


            space = False
    else:
        space = True
    screen.fill((0,0,0))
    #square.squre_draw(dense, surface, res_X, res_Y, randX1 + xp, randY1 + yp, randX2 + xp, randY2 + yp, randX3 + xp, randY3 + yp, randX4 + xp, randY4 + yp, (colorr,colorg,colorb))
    square.triangle_draw(dense, surface, res_X, res_Y, randX1 + xp, randY1 + yp, randX2 + xp, randY2 + yp, randX3 + xp, randY3 + yp,(colorr,colorg,colorb))


    if keys[pygame.K_d]:
                xp += 1
    if keys[pygame.K_a]:
                xp += -1
    if keys[pygame.K_w]:
                yp += -1
    if keys[pygame.K_s]:
                yp += 1

            
            #square.squre_draw(surface, res_X, res_Y, 
                              #(100 + Xx), (100+Yy),
                              # (-100+ Xx), (100+Yy), 
                              # (-100+ Xx),  (-120+Yy),
                                #(100+Xx), (80+Yy), (255,255,255))



    block.rect.clamp_ip(screen.get_rect())
    #screen.fill((0, 0, 0))
    #screen.blit(block.image, block.rect)
    pygame.display.flip()
    running = False