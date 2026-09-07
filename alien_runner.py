import pygame
from sys import exit
from random import randint, choice

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         alien_1 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_run/alien_run01.png").convert_alpha()
#         alien_2 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_run/alien_run02.png").convert_alpha()
#         alien_3 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_run/alien_run03.png").convert_alpha()
#         alien_4 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_run/alien_run04.png").convert_alpha()
#
#         alien_jump1 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_jump/alien_jump01.png").convert_alpha()
#         alien_jump2 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_jump/alien_jump02.png").convert_alpha()
#         alien_jump3 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_jump/alien_jump03.png").convert_alpha()
#         alien_jump4 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_jump/alien_jump04.png").convert_alpha()
#
#         self.alien_animation_index = 0
#         self.jump_index = 0
#         self.gravity = 0
#         self.alien_frames = [alien_1, alien_2, alien_3, alien_4]
#         self.jump_frames = [alien_jump1, alien_jump2, alien_jump3, alien_jump4]
#         self.jump_image = self.jump_frames[self.jump_index]
#         self.image = self.alien_frames[self.alien_animation_index]
#         self.rect = self.image.get_rect(midbottom = (100, 320))
#
#     def alien_input(self):       
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE] and self.rect.bottom <= 320:
#             print("class space")
#     def apply_gravity(self):
#         self.gravity -= 1
#         self.rect.y -= self.gravity
#         if self.rect.bottom >= 320:
#             self.rect.bottom = 320
#
#     def animation(self):
#         if self.rect.bottom < 320:
#             self.jump_index += 0.1
#             if self.jump_index > len(self.jump_frames):
#                 self.jump_index = 0
#             self.jump_image = self.jump_frames[self.jump_index]
#         else:
#             self.alien_animation_index += 0.2
#             if self.alien_animation_index > len(self.alien_frames):
#                 self.alien_animation_index = 0
#             self.image = self.alien_frames[int(self.alien_animation_index)]
#
#     def update(self):
#         self.alien_input()
#         self.apply_gravity()
#         self.animation()

             



def score_management(): 
    current_score = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = text_font.render(f"Score: {current_score}", False, "green")
    score_rect = score_surf.get_rect(center = (350, 40))
    screen.blit(score_surf, score_rect)
    return current_score

def enemy_movement(enemy_list, speed):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.x += int(speed)
            if enemy_rect.bottom == 320:
                screen.blit(knife_surf, enemy_rect)
            else:
                screen.blit(skull_surf, enemy_rect)
        enemy_list = [enemy for enemy in enemy_list if enemy.x > -100]
        return enemy_list
    else:
        return []


def alien_animation():
    global alien_surf, alien_run_index, alien_jump_surf, alien_jump_index
    
    if alien_rect.bottom < 300:
        alien_jump_index += 0.1
        if alien_jump_index >= len(alien_jump):
            alien_jump_index = 0
        alien_jump_surf = alien_jump[int(alien_jump_index)]
         
    else:
        alien_run_index += 0.2 
        if alien_run_index >= len(alien_run):
            alien_run_index = 0
        alien_surf = alien_run[int(alien_run_index)]         

def collision_x(alien, enemy):
    if enemy:
        for enemy_rect in enemy:
            if alien.colliderect(enemy_rect):
                return False
    return True

pygame.init()
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Alien Runner")
text_size = 30
text_font = pygame.font.Font("/data/data/com.termux/files/home/Desktop/alien_game/PixelifySans-VariableFont_wght.ttf", text_size)
clock = pygame.time.Clock()
game_active = False

# player = pygame.sprite.GroupSingle()
# player.add(Player())

#Sky
sky_surf = pygame.Surface((700, 400))
sky_surf.fill("#1e3b1b")

#Ground
ground_surf = pygame.Surface((700, 100))
ground_surf.fill("#707b6f")

#BUTTONS
#Jump
jump_btn_surf = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/Jump_btm.png")
jump_btn_rect = jump_btn_surf.get_rect(midleft = (20, 360))

#Restart
restart_surf = text_font.render("RESTART", False, "white")
restart_rect = restart_surf.get_rect(bottomleft = (15, 390))

#Quit
quit_surf = text_font.render("QUIT", False, "white")
quit_rect = quit_surf.get_rect(bottomright = (685, 390))

#A|ien
alien_1 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_run/alien_run01.png").convert_alpha()
alien_2 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_run/alien_run02.png").convert_alpha()
alien_3 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_run/alien_run03.png").convert_alpha()
alien_4 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_run/alien_run04.png").convert_alpha()
alien_run = [alien_1, alien_2, alien_3, alien_4]
alien_run_index = 0
alien_surf = alien_run[alien_run_index]
alien_rect = alien_surf.get_rect(midbottom = (150, 320))

alien_jump1 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_jump/alien_jump01.png").convert_alpha()
alien_jump2 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_jump/alien_jump02.png").convert_alpha()
alien_jump3 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_jump/alien_jump03.png").convert_alpha()
alien_jump4 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/alien_jump/alien_jump04.png").convert_alpha()
alien_jump = [alien_jump1, alien_jump2, alien_jump3, alien_jump4]
alien_jump_index = 0
alien_jump_surf = alien_jump[alien_jump_index]
alien_jump_rect = alien_jump_surf.get_rect(midbottom = (150, 320))


dead_alien_surf = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/dead_alien.png")
dead_alien_surf = pygame.transform.rotozoom(dead_alien_surf, 0, 3)
dead_alien_rect = dead_alien_surf.get_rect(center = (320, 240))

alien_gravity = 0

#Knife
knife01 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/knife/knife01.png")
knife02 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/knife/knife02.png")
knife03 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/knife/knife03.png")
knife04 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/knife/knife04.png")
knife_frames = [knife01, knife02, knife03, knife04]
knife_frame_index = 0
knife_surf = knife_frames[knife_frame_index]

#Flying Skull
skull01 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/skull/flying_skull01.png")
skull02 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/skull/flying_skull02.png")
skull03 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/skull/flying_skull03.png")
skull04 = pygame.image.load("/data/data/com.termux/files/home/Desktop/alien_game/skull/flying_skull04.png")
skull_frames = [skull01, skull02, skull03, skull04]
skull_frame_index = 0
skull_surf = skull_frames[skull_frame_index]

#MDied Message
you_died_surf = text_font.render("[You died]", False, "red")
you_died_rect = you_died_surf.get_rect(center = (350, 50))

#Alien thumbnail
thumbnail_surf = pygame.image.load("/data/data/com.termux/files/home/storage/pictures/Alien_20260716200255.png")
thumbnail_rect = thumbnail_surf.get_rect(center = ((screen.get_width() / 2), (screen.get_height() / 2)))


#Score Management
start_time = 0
score = 0

level = 1

speed_x = -6
enemy_rect_list = []

#Double jump
double_jump = 2

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1000)

knife_timer = pygame.USEREVENT + 2
pygame.time.set_timer(knife_timer, 100)

skull_timer = pygame.USEREVENT + 3
pygame.time.set_timer(skull_timer, 200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jump_btn_rect.collidepoint(event.pos) and alien_rect.bottom == 320 and double_jump > 0:
                    alien_gravity = -17
                    double_jump -= 1
                if jump_btn_rect.collidepoint(event.pos) and alien_rect.bottom < 320 and double_jump > 0:
                    alien_gravity = -15
                    double_jump -= 1
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and alien_rect.bottom == 320 and double_jump > 0:
                    alien_gravity = -17
                    double_jump -= 1
                    print("space")
                if event.key == pygame.K_SPACE and alien_rect.bottom < 320 and double_jump > 0:
                    alien_gravity = -15
                    double_jump -= 1
            
            dj_surf = text_font.render(f"Double Jump: {double_jump}/2", False, "green")
            dj_rect = dj_surf.get_rect(midleft = (140, 360))

                
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if thumbnail_rect.collidepoint(event.pos) and score == 0:
                    game_active = True
                    score = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos) and score > 0:
                    game_active = True
                    alien_rect.bottom = 320
                    start_time = int(pygame.time.get_ticks() / 1000)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(event.pos) and score > 0:
                    pygame.quit()
                    exit()

            
        if game_active:
            if event.type == enemy_timer:
                if randint(0, 2) == 1:
                    enemy_rect_list.append(knife_surf.get_rect(bottomright = (randint(900, 1100), 320)))
                else:
                    enemy_rect_list.append(skull_surf.get_rect(bottomright = (randint(900, 1100), 130)))

                
            if event.type == knife_timer:
                knife_frame_index = (knife_frame_index + 1) % len(knife_frames)

                knife_surf = knife_frames[int(knife_frame_index)]
            
            if event.type == skull_timer:
                skull_frame_index = (skull_frame_index + 1) % len(skull_frames)
                skull_surf = skull_frames[int(skull_frame_index)]
    
    
    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 320))
        screen.blit(jump_btn_surf, jump_btn_rect)

        screen.blit(dj_surf, dj_rect)
        pygame.draw.line(screen, "white", (0, 320), (700, 320), 2)
        

        score = score_management()

        # knife_rect.x -= 7
        # if knife_rect.right <= 0:
        #     knife_rect.left = 700    
        # screen.blit(knife_surf, knife_rect)
     
        alien_gravity += 0.9
        alien_rect.y += alien_gravity
        if alien_rect.bottom >= 320:
            alien_rect.bottom = 320

        if (double_jump == 0 and alien_rect.bottom == 320) or (double_jump == 1 and alien_rect.bottom == 320):
            double_jump = 2


        alien_animation()
        enemy_rect_list = enemy_movement(enemy_rect_list, speed_x)  
        screen.blit(alien_surf if alien_rect.bottom >= 320 else alien_jump_surf, alien_rect)
        # player.draw(screen)
        # player.update()

        game_active = collision_x(alien_rect, enemy_rect_list)
        level_surf = text_font.render(f"Level: {level}", False, "green")
        level_rect = level_surf.get_rect(midleft = (20, 40))
        if score == 10:
            #2
            level = 2
            speed_x = -8
        if score == 20:
            #3
            level = 3
            speed_x = -10

        if score == 30:
            #4
            level = 4
            speed_x = -12
        if score == 50:
            #5
            level = 5
            speed_x = -15
        screen.blit(level_surf, level_rect)

    else:
        enemy_rect_list.clear()        
        speed_x = -6
        level = 1

        total_score = text_font.render(f"Total score: {score}", False, "green")
        total_rect = total_score.get_rect(center = (350, 100))
        game_name = text_font.render("Alien Runner", False, "black")
        game_name_rect = game_name.get_rect(center = ((screen.get_width() / 2), 50))
        start_surf = text_font.render("Click the alien head to start!", False, "black")
        start_rect = start_surf.get_rect(center = ((screen.get_width() / 2), 350))        
        
        if score > 0:
            screen.fill("#560909")
            screen.blit(dead_alien_surf, dead_alien_rect)
            screen.blit(you_died_surf, you_died_rect)
            screen.blit(total_score, total_rect)
            screen.blit(restart_surf, restart_rect)
            screen.blit(quit_surf, quit_rect)
        else:
            screen.fill("#42d727")
            screen.blit(thumbnail_surf, thumbnail_rect)
            screen.blit(game_name, game_name_rect)
            screen.blit(start_surf, start_rect)
        
    
    
    pygame.display.update()
    clock.tick(60)
