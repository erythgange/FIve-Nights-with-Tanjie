import pygame
import random
import sys
from pygame import mixer
# constants
pygame.init()
WIDTH, HEIGHT = 1920, 1080
FPS = 60
CAMERA_SPEED = 5
ENEMY_SPAWN_RATE = 100  # Lower is faster
ENEMY_HIT_RADIUS = 50

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)

# font 
font = pygame.font.Font(None, 36)
# displays
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Five Nights with Tanjie")
# Tanjie idle/crouch
Tidle = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tidle.png').convert_alpha()
Tcrouch = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch.png').convert_alpha()
Tidle_crouch = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tidle-crouch.png').convert_alpha()
Tidle_crouchM = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tidle-crouchM.png').convert_alpha()
Tcrouch_idle = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch-idle.png').convert_alpha()
Tcrouch = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch.png').convert_alpha()
Tcrouch_switch = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch-switch.png').convert_alpha()
# Tanjie attack
Tcrouch_attacklong = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch-attacklong.png').convert_alpha()
Tcrouch_attackshort = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch-attackshort.png').convert_alpha()
Tattacklong_crouch = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-crouch.png').convert_alpha()
# Tanjie miss
Tattacklong_miss1 = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-miss1.png').convert_alpha()
Tattacklong_miss2 = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-miss2.png').convert_alpha()
Tattacklong_miss3 = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-miss3.png').convert_alpha()
Tattacklong_miss4 = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-miss4.png').convert_alpha()
Tmiss_crouchM = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tmiss-crouchM.png').convert_alpha()
# Tanjie hit/hurt
Thit1 = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Thit1.png').convert_alpha()
Thit2 = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Thit2.png').convert_alpha()
Thit2_crouchM = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Thit2-crouchM.png').convert_alpha()
Thit2_attacklong = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Thit2-attacklong.png').convert_alpha()
Thit2_attacklongM = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Thit2-attacklongM.png').convert_alpha()
Thurt = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Thurt.png').convert_alpha()
# Tanjie mirror frames
mirror_frames = [Tidle_crouchM, Tmiss_crouchM, Tcrouch_switch, Thit2_crouchM, Thit2_attacklongM, Tattacklong_crouch, Tattacklong_miss1]
# BG
Light = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Light.png').convert_alpha()
BG = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/BG.png').convert()
Ridle = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Ridle.png').convert_alpha()

# BG music
mixer.music.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/BGX.mp3')
mixer.music.play(-1)

# constants
constant_y = 600




# class enemy
class Enemy:
    def __init__(self,tanjie):
        self.x = (random.choice([1000,-1000])) + 700 + tanjie.x
        self.speed = 10# + random.randint(-1,1)
        #if spawned from tanjie's left:(self.x < tanjie_x), go right. vice versa
        if self.x < tanjie.x: self.direction = 1  
        else: self.direction = -1
        self.collision_rect = pygame.Rect(0,0,100,25)
        

    def move(self): self.x += self.speed * self.direction
    def draw(self,tanjie): 
        
        finalx = (self.x - (tanjie.x))
        finaly = constant_y - (Ridle.get_height()/2)
        
        center = (finalx, finaly)
        if self.direction == -1: screen.blit(pygame.transform.flip(Ridle, True, False), center)
        else: screen.blit(Ridle, center)        
        pygame.draw.circle(screen, RED, (finalx + Ridle.get_width()/2, constant_y), 5) # debug circle
        
        # collisions
        self.collision_rect.center = (finalx+ 250, constant_y+100)
        if self.collision_rect.colliderect(tanjie.collision_rect):
            color = GREEN
        #    tanjie.collide(self.x)
            #print("hit")
        else: color = RED    
        
        pygame.draw.rect(screen, color, self.collision_rect)
        


    def is_hit(self, pos): return (pos[0] - self.x) ** 2 + (pos[1] - constant_y) ** 2 < ENEMY_HIT_RADIUS ** 2


# class player
class Player:
    def __init__(self):
        
        # experiment variables (can change)
        self.framepause : int = 6 # how fast (ms) Tanjie moves every frame
        self.inactive : int = 2000 # how much time (ms) Tanjie returns to idle pose after moving
        self.speed : float = 40

        # constant variables (dont change)
        self.x : int = 0
        self.y : int = 0
        self.velocity_x : float = 0
        self.velocity_y : float = 0
        self.can_attack : bool = True
        self.looking_left : bool = True
        self.time_last_move : int = 0
        self.actions = [Tidle]
        self.frameduration = self.framepause
        self.collision_rect = pygame.Rect(0,0,100,25)
        self.collision_color = GREEN
        self.freejump : int = 1

    def move(self, direction:str, keydown:bool = True):
        
        def attacklong():
                self.actions.append(Tcrouch_attacklong)
                self.actions.append(Tcrouch_attacklong)
                self.actions.append(Tattacklong_crouch)
                if self.freejump > 0: 
                    self.freejump -= 1
                    self.actions.append(Tcrouch)
                else:
                    self.actions.append(Tattacklong_miss1)
                    self.actions.append(Tattacklong_miss2)
                    self.actions.append(Tattacklong_miss3)
                    self.actions.append(Tattacklong_miss4)
                    self.actions.append(Tmiss_crouchM)
                    self.actions.append(Tcrouch)
                
        if keydown == True and self.can_attack == True:
            self.can_attack = False # no spamming attack

            #from a successful hit,
            if self.actions[0] == Thit2 or self.actions[0] == Thit1:
                self.freejump : int = 1
                preserve = self.actions[0]
                self.actions.clear() # clear everything except first
                self.actions.insert(0, preserve)
                #same direction
                if (direction == "left" and self.looking_left == True) or (direction == "right" and self.looking_left == False): 
                    if self.actions[0] == Thit2: self.actions.append(Thit2_attacklong)
                #opposite direction
                if (direction == "right" and self.looking_left == True) or (direction == "left" and self.looking_left == False): 
                    if self.actions[0] == Thit2: self.actions.append(Thit2_attacklongM)
                    else: self.looking_left = not self.looking_left
                
                attacklong()

            # from idle
            if self.actions[0] == (Tidle):
                if (direction == "left" and self.looking_left == True) or (direction == "right" and self.looking_left == False): 
                    self.actions.append(Tidle_crouch) # to crouch left
                if (direction == "right" and self.looking_left == True) or (direction    == "left" and self.looking_left == False): 
                    self.actions.append(Tidle_crouchM) # to crouch right
                self.actions.append(Tcrouch) # hold crouch
                attacklong()
                
            # from crouch
            if self.actions[0] == Tcrouch:
                if (direction == "left" and self.looking_left == False) or (direction == "right" and self.looking_left == True):
                    self.actions.append(Tcrouch_switch) # if attacking behind, turn around first, then
                attacklong() # long jumping attack

            # hitstop: pygame.time.delay(1000) # hitstop
    
    def collide(self, target_pos): 
        if self.actions[0] == (Tcrouch_attacklong): #if jumping
            self.actions.clear()
            self.actions.append(Thit1)
            self.actions.append(Thit1)
            self.actions.append(Thit1)
            self.actions.append(Thit2)
            self.actions.append(Thit2)
            self.actions.append(Thit2_crouchM)
            self.actions.append(Tcrouch)
        else:
            self.actions.clear()
            self.actions.append(Thurt)
            self.actions.append(Thurt)
            self.actions.append(Thurt)
            self.actions.append(Tcrouch)

    def draw(self):        

        # animation frame rate / edit it with self.framepause
        if len(self.actions) > 1: # if there is an appended action, 
            self.frameduration -= 1 # start countdown.

            if self.frameduration == 0: # if countdown reaches zero,
                self.actions.pop(0) # proceed to next action and
                self.frameduration = self.framepause # start countdown again
                
                # if tanjie does an action that turns him around
                if self.actions[0] in mirror_frames: self.looking_left = not self.looking_left
                self.time_last_move = pygame.time.get_ticks() # timer after this move

                # if crouching (vulnerable)
                if self.actions[0] == (Tidle_crouch or Tidle_crouchM):
                    self.collision_rect = pygame.Rect(0,0,25,25)
                # attack recovery
                if self.actions[0] == Thit2_crouchM:
                    if self.looking_left == False: self.velocity_x = -(self.speed) # going right    
                    else: self.velocity_x = (self.speed) # going left
                # miss recovery
                if self.actions[0] == Tmiss_crouchM:
                    if self.looking_left == False: self.velocity_x = -(self.speed/2)    
                    else: self.velocity_x = (self.speed/2)
                #free jumps when
                if self.actions[0] in [Tattacklong_miss4, Thit1] :
                    self.freejump = 1
                    self.can_attack = True


            # success hit
            if self.actions[0] == Thit2:
                self.velocity_y = -20
                if self.looking_left == False: self.velocity_x = (self.speed/2) # going right    
                else: self.velocity_x = -(self.speed/2) # going left
            
            # if jumping attack
            if self.actions[0] == Tcrouch_attacklong:
                
                if self.looking_left == False: self.velocity_x = self.speed # going right    
                else: self.velocity_x = -self.speed # going left
                self.collision_rect = pygame.Rect(0,0,25,25)
            

        else: 
            self.can_attack = True # if there is no appended action, tanjie can now attack
            self.collision_rect = pygame.Rect(0,0,25,25)

        # velocity_x formulas
        self.x += self.velocity_x
        #self.y += self.velocity_y + constant_y
        self.y += self.velocity_y
        self.velocity_x *= 0.9
        self.velocity_y *= 0.9

        # collisions
        self.collision_rect.center = (960, constant_y+100)
        pygame.draw.rect(screen, self.collision_color, self.collision_rect)
        
        # idle animation
        elapsed_time = ((pygame.time.get_ticks() - self.time_last_move)) # timer start after last move
        if (self.actions[0] == Tcrouch) and (elapsed_time > self.inactive): # if tanjie is crouching, and timer is up, 
            self.actions[0] = (Tcrouch_idle) # transition back to idle animation
            self.actions.append(Tidle)

        # image divided by 2, on (x,y), marksk the center point
        center = ((WIDTH/2 - 250) + self.velocity_x, self.velocity_y + constant_y - 125)
        if self.looking_left == True: screen.blit(self.actions[0], center) # looking left
        else: screen.blit(pygame.transform.flip(self.actions[0], True, False), center) # looking right
        pygame.draw.circle(screen, RED, (WIDTH/2, constant_y), 5) # debug circle

# main
def main():
    clock = pygame.time.Clock()
    tanjie = Player()
    enemies = [] #must be enemy class
    killed_enemies = []
    score = 0
    spawn_counter = 0

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: tanjie.move("left")
                if event.key == pygame.K_RIGHT: tanjie.move("right")

        # enemies
        spawn_counter += 1
        if spawn_counter >= ENEMY_SPAWN_RATE:
            enemies.append(Enemy(tanjie))
            spawn_counter = 0
        for enemy in enemies:
            enemy.move()

        # drawing
        def cam_offset(inputpos, parralax=1):
            inputpos = (inputpos - tanjie.x) * parralax
            return inputpos
        
        bglocation = cam_offset(-4000)
        screen.fill(WHITE)
        screen.blit(BG, (bglocation, 1))
        tanjie.draw()
        for enemy in enemies: enemy.draw(tanjie)
        
        # collisions
        for enemy in enemies:
            if tanjie.collision_rect.colliderect(enemy.collision_rect):
                tanjie.collide(enemy.x)
                enemies.remove(enemy)
                tanjie.collision_color = GREEN
            else: tanjie.collision_color = WHITE






        # debugging
        score_text = font.render(f'Score: {score}', True, GREEN)
        screen.blit(score_text, (10, 10))
        
        clock.tick(FPS)
        fps_text = font.render(f'FPS: {round(clock.get_fps())}', True, GREEN)
        screen.blit(fps_text, (10, 40))
        
        debug1 = font.render(f'tanjie_x: {round(tanjie.x,1)}', True, GREEN)
        screen.blit(debug1, (10, 70))
        
        debug2 = font.render(f'looking left: {(tanjie.looking_left)}', True, GREEN)
        screen.blit(debug2, (10, 100))
        
        debug3 = font.render(f'tanjie velocity_x: {round(tanjie.velocity_x,1)}', True, GREEN)
        screen.blit(debug3, (10, 130))
        debug4 = font.render(f'tanjie velocity_y: {round(tanjie.velocity_y,1)}', True, GREEN)
        screen.blit(debug4, (10, 160))
        debug5 = font.render(f'tanjie free jump: {round(tanjie.freejump,1)}', True, GREEN)
        screen.blit(debug5, (10, 190))
        
        
        pygame.display.flip()
        
# menu
while True : 
    # menu background
    bg_menu = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/BG.png').convert_alpha()
    screen.blit(bg_menu, (-4022, 22))

    # title 
    title_img = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/FNWT_Logo_Transparent.png').convert_alpha()
    screen.blit(title_img, (500, -300))

    #   tanji background
    tanji_img = pygame.image.load('/mnt/c/users/user/Desktop/FIve-Nights-with-Tanjie/Assets/Tidle.png').convert_alpha()
    screen.blit(tanji_img, (700, 500))
    #title_text = font.render("Five Nights with Tanjie", True, WHITE)
    #title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 10))
    #screen.blit(title_text, title_rect)

    # menu options
    play_text = font.render("< TO PLAY >", True, WHITE)
    play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
    screen.blit(play_text, play_rect)

    quit_text = font.render("Q TO QUIT ", True, WHITE)
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.40))
    screen.blit(quit_text, quit_rect)

    pygame.display.flip()

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    main()
                elif event.key == pygame.K_RIGHT:
                    main()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

asdasd
# start game
main()