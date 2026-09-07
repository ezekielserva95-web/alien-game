import pygame

pygame.init()
screen = pygame.display.set_mode((500, 200))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("space")
