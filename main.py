import pygame

pygame.init()   

window_width=700
window_height=400

BLACK = (0, 0, 0)
FPS=30

size = (window_width, window_height)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("World Map")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
run = True

clock = pygame.time.Clock()

background_image0 = pygame.image.load("a.png").convert()
background_image1 = pygame.image.load("b.png").convert()
background_image2 = pygame.image.load("c.png").convert()
background_image3 = pygame.image.load("d.png").convert()
background_image4 = pygame.image.load("e.png").convert()
background_image5 = pygame.image.load("f.png").convert()
background_image6 = pygame.image.load("g.png").convert()
background_image7 = pygame.image.load("h.png").convert()
background_image8 = pygame.image.load("i.png").convert()
background_image9 = pygame.image.load("j.png").convert()
dx=5
dy=5
by=0
bx0=0
bx1=window_width
bx2=1400
bx3=2100
bx4=2800
bx5=3500
bx6=4200
bx7=4900
bx8=5600
bx9=6300
while run:  
     # keep loop running at the right speed
    clock.tick(FPS)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
   

    
    screen.blit(background_image0, [bx0, by])
    screen.blit(background_image1, [bx1, by])
    screen.blit(background_image2, [bx2, by])
    screen.blit(background_image3, [bx3, by])
    screen.blit(background_image4, [bx4, by])
    screen.blit(background_image5, [bx5, by])
    screen.blit(background_image6, [bx6, by])
    screen.blit(background_image7, [bx7, by])
    screen.blit(background_image8, [bx8, by])
    screen.blit(background_image9, [bx9, by])

    pygame.display.update() 

    bx0 -=dx
    bx1 -=dx
    bx2-=dx
    bx3-=dx
    bx4-=dx
    bx5-=dx
    bx6-=dx
    bx7-=dx
    bx8-=dx
    bx9-=dx

    if bx0 <=-window_width:
        bx0=6300

    if bx1 <=-window_width:
        bx1=6300

    if bx2 <=-window_width:
        bx2=6300
    
    if bx3 <=-window_width:
        bx3=6300

    if bx4 <=-window_width:
        bx4=6300

    if bx5 <=-window_width:
        bx5=6300

    if bx6 <=-window_width:
        bx6=6300

    if bx7 <=-window_width:
        bx7=6300

    if bx8 <=-window_width:
        bx8=6300

    if bx9 <=-window_width:
        bx9=6300

pygame.quit()


