import math

import pygame
from pygame.locals import *


pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH, HEIGHT = 700, 700


screen = pygame.display.set_mode((WIDTH, HEIGHT))
spin = pygame.image.load("spin.png")
spin = pygame.transform.scale(spin, (500, 500))
rect = spin.get_rect(center=(WIDTH/2, HEIGHT/2))

circle = pygame.draw.circle(screen, RED, rect.center, 50, 0)
print(rect.collidepoint((100, 100)))
FPS = 60
clock = pygame.time.Clock()

angle = 0
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
            
    mouse = pygame.mouse.get_pos()
    # print(pygame.MOUSEBUTTONDOWN)
    # if rect.collidepoint(mouse):
    #     print(mouse)
    # print(type(mouse))
        
    # new_spin = pygame.transform.rotate(spin, -angle)
    # new_rect = new_spin.get_rect(center=rect.center)
    # angle=(angle+1)%360
    
    screen.fill(WHITE)
    # pygame.draw.rect(screen, RED, rect)
    r = 100
    circle = pygame.draw.circle(screen, RED, rect.center, r, 0)
    screen.blit(spin, rect)
    x1, y1 = mouse
    x2, y2 = circle.center
    
    distanse = math.hypot(x1-x2, y1-y2)
    if distanse<=r:
        print("touch")
        
    else:
        print("No!")
    # print(circle.collidepoint(mouse))
    # screen.blit(new_spin, new_rect)
    pygame.display.update()
    
    
pygame.quit()