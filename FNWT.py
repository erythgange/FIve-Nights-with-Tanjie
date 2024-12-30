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
BLACK = (0,0,0)

# displays
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Five Nights with Tanjie")

# assets
font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()
# Tanjie idle/crouch
Tidle = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tidle.png').convert_alpha()
Tcrouch = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch.png').convert_alpha()
Tidle_crouch = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tidle-crouch.png').convert_alpha()
Tidle_crouchM = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tidle-crouchM.png').convert_alpha()
Tcrouch_idle = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch-idle.png').convert_alpha()
Tcrouch = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch.png').convert_alpha()
Tcrouch_switch = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch-switch.png').convert_alpha()
# Tanjie attack
Tcrouch_attacklong0 = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch-attacklong0.png').convert_alpha()
Tcrouch_attacklong = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch-attacklong.png').convert_alpha()
Tattacklong_land_attacklong = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-land-attacklong.png').convert_alpha()
Tattacklong_landM_attacklong = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-landM-attacklong.png').convert_alpha()
Tcrouch_attackshort = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tcrouch-attackshort.png').convert_alpha()
Tattacklong_crouch = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-crouch.png').convert_alpha()
# Tanjie miss
Tattacklong_miss1 = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-miss1.png').convert_alpha()
Tattacklong_miss2 = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-miss2.png').convert_alpha()
Tattacklong_miss3 = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-miss3.png').convert_alpha()
Tattacklong_miss4 = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tattacklong-miss4.png').convert_alpha()
Tmiss_crouchM = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Tmiss-crouchM.png').convert_alpha()
# Tanjie hit/hurt
Thit1 = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Thit1.png').convert_alpha()
Thit2 = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Thit2.png').convert_alpha()
Thit2_crouchM = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Thit2-crouchM.png').convert_alpha()
Thit2_attacklong = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Thit2-attacklong.png').convert_alpha()
Thit2_attacklongM = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Thit2-attacklongM.png').convert_alpha()
Thurt = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Thurt.png').convert_alpha()
# Tanjie mirror frames
mirror_frames = [Tattacklong_landM_attacklong, Tidle_crouchM, Tmiss_crouchM, Tcrouch_switch, Thit2_crouchM, Thit2_attacklongM, Tattacklong_crouch, Tattacklong_miss1]
# Menu
FNWT_Logo = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/FNWT_Logo_Transparent.png').convert_alpha()
FNWT_Logo = pygame.transform.scale(FNWT_Logo,(FNWT_Logo.get_width()/2,FNWT_Logo.get_height()/2))
Menu = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Menu.png').convert_alpha()
Menu = pygame.transform.scale(Menu,(Menu.get_width()/1.5,Menu.get_height()/1.5))
# FG
FG1 = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/FG1.png').convert_alpha()
FG2 = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/FG2.png').convert_alpha()
FG3 = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/FG3.png').convert_alpha()
# BG
LampLight = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/LampLight.png').convert_alpha()
LampPost = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/LampPost.png').convert_alpha()
Street = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/BG.png').convert()
Ridle = pygame.image.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/Ridle.png').convert_alpha()

# BG music
mixer.music.load('/mnt/c/users/user/desktop/FIve-Nights-with-Tanjie/Assets/BGX.mp3')
mixer.music.play(-1)

# constants
constant_y = 600
game_started = False

total_game_seconds = 15 * 60 
seconds_per_game_hour = 30
start_time = 0
end_time = 6


# clock frame rate
clock = pygame.time.Clock()

def time_format(hour, minute):
    period = "AM" if hour < 12 else "PM"
    formatted_hour = hour if hour != 0 else 12
    return f"{formatted_hour:02}:{minute:02}{period}"

def get_time(elapsed_seconds) : 
    game_hours = int(elapsed_seconds // seconds_per_game_hour)
    game_minutes = int((elapsed_seconds % seconds_per_game_hour) / (seconds_per_game_hour / 60 ))
    return (start_time + game_hours, game_minutes)

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
        #pygame.draw.circle(screen, RED, (finalx + Ridle.get_width()/2, constant_y), 5) # debug circle
        
        # collisions
        self.collision_rect.center = (finalx+ 250, constant_y+100)
        if self.collision_rect.colliderect(tanjie.collision_rect):
            color = GREEN
        #    tanjie.collide(self.x)
            #print("hit")
        else: color = RED    
        
        #pygame.draw.rect(screen, color, self.collision_rect)
        


    def is_hit(self, pos): return (pos[0] - self.x) ** 2 + (pos[1] - constant_y) ** 2 < ENEMY_HIT_RADIUS ** 2


# class player
class Player:
    def __init__(self):
        
        # experiment variables (can change)
        self.framepause : int = 8 # how fast (ms) Tanjie moves every frame
        self.inactive : int = 2000 # how much time (ms) Tanjie returns to idle pose after moving
        self.speed : float = 30

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
        self.freejump : int = 2
        self.invulnerable = False

    def move(self, direction:str, keydown:bool = True):
        def attacklong():
                self.actions.append(Tcrouch_attacklong)
                self.actions.append(Tattacklong_crouch)
                if self.freejump > 0: 
                    self.actions.append(Tcrouch)
                else:
                    self.actions.append(Tattacklong_miss1)
                    self.actions.append(Tattacklong_miss2)
                    self.actions.append(Tattacklong_miss2)
                    self.actions.append(Tattacklong_miss3)
                    self.actions.append(Tattacklong_miss3)
                    self.actions.append(Tattacklong_miss3)
                    self.actions.append(Tattacklong_miss4)
                    self.actions.append(Tattacklong_miss4)
                    self.actions.append(Tmiss_crouchM)
                    self.actions.append(Tcrouch)
                
        if keydown == True:#and self.can_attack == True:
            self.can_attack = False # no spamming attack
            
            # if jump attacking,
            if self.actions[0] == Tcrouch_attacklong and self.freejump > 0:
                self.freejump -= 1
                self.actions.clear()
                #same direction
                if (direction == "left" and self.looking_left == True) or (direction == "right" and self.looking_left == False): 
                    self.actions.append(Tattacklong_land_attacklong)
                    self.looking_left = not self.looking_left
                    attacklong()
                #opposite direction
                if (direction == "right" and self.looking_left == True) or (direction == "left" and self.looking_left == False): 
                    self.actions.append(Tattacklong_landM_attacklong)
                    self.frameduration = 10
                    self.looking_left = not self.looking_left
                    self.actions[0]
                    attacklong()

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
                    else: 
                        self.actions.append(Tattacklong_landM_attacklong)
                        #self.looking_left = not self.looking_left
                
                attacklong()

            # from idle
            if self.actions[0] == (Tidle):
                if (direction == "left" and self.looking_left == True) or (direction == "right" and self.looking_left == False): 
                    self.actions.append(Tidle_crouch) # to crouch left
                if (direction == "right" and self.looking_left == True) or (direction    == "left" and self.looking_left == False): 
                    self.actions.append(Tidle_crouchM) # to crouch right
                self.actions.append(Tcrouch) # hold crouch
                self.actions.append(Tcrouch_attacklong0)
                attacklong()
                
            # from crouch
            if self.actions[0] == Tcrouch:
                if (direction == "left" and self.looking_left == False) or (direction == "right" and self.looking_left == True):
                    self.actions.append(Tcrouch_switch) # if attacking behind, turn around first, then
                self.actions.append(Tcrouch_attacklong0)
                attacklong() # long jumping attack
                
    def collide(self, target_pos): 
        #self.velocity_x /= 1.1
        self.freejump = 2
        self.x += self.velocity_x
        if self.actions[0] == (Tcrouch_attacklong): #if jumping
            self.invulnerable = True
            self.actions.clear()
            self.actions.append(Thit1)
            self.actions.append(Thit2)
            self.actions.append(Thit2)
            self.actions.append(Thit2)
            #self.actions.append(Thit2_crouchM)
            self.actions.append(Tattacklong_landM_attacklong)
            self.actions.append(Tcrouch)
        elif self.invulnerable == False:
            self.actions.clear()
            self.actions.append(Thurt)
            self.actions.append(Thurt)
            self.actions.append(Thurt)
            self.actions.append(Tcrouch)

    def draw(self):        
        # animation frame rate / edit it with self.framepause
        if len(self.actions) > 1: # if there is an appended action, 
            self.frameduration -= 1 # start countdown.
            def applyvelocity(if_looking_left,if_looking_right):
                if self.looking_left == False: self.velocity_x = if_looking_left # going right    
                else: self.velocity_x = if_looking_right # going left
            if self.frameduration == 0: # if countdown reaches zero,
                self.actions.pop(0) # proceed to next action and
                self.frameduration = self.framepause # start countdown again
                # if tanjie does an action that turns him around
                if self.actions[0] in mirror_frames: self.looking_left = not self.looking_left
                self.time_last_move = pygame.time.get_ticks() # timer after this move
                # vulnerable frames
                if self.actions[0] in [Tcrouch, Tattacklong_miss1]:
                    self.invulnerable = False
                # if attack land attack
                if self.actions[0] in [Tattacklong_land_attacklong, Tattacklong_landM_attacklong]:
                    self.velocity = 0
                # attack recovery
                if self.actions[0] == Thit2_crouchM: applyvelocity(-(self.speed/2), (self.speed/2))
                # miss recovery
                if self.actions[0] == Tmiss_crouchM: applyvelocity(-(self.speed/2), (self.speed/2))
                #free jumps when
                if self.actions[0] in [Tattacklong_miss4, Thit1] :
                    self.freejump = 2
                    self.can_attack = True
                #jumping attack(once)
                if self.actions[0] == Tcrouch_attacklong:
                    x = self.speed - self.freejump
                    applyvelocity(x, -x)
                    self.frameduration *= 4
                    self.frameduration -= self.freejump*2
                #longattack, interrupt, long attack
                if self.actions[0] == Tattacklong_land_attacklong:
                    applyvelocity((self.speed), -(self.speed))
                if self.actions[0] == Tmiss_crouchM:
                    self.actions.clear()
                    self.actions.insert(0, Tmiss_crouchM)
                    self.actions.append(Tcrouch)

            # success hit
            if self.actions[0] == Thit2:
                self.velocity_y = -20
                applyvelocity((self.speed/4), -(self.speed/4))
            
            # just before attack
            if self.actions[0] == Tcrouch_attacklong0:
                applyvelocity(-self.speed/2, self.speed/2)

        else: 
            self.can_attack = True # if there is no appended action, tanjie can now attack
            self.collision_rect = pygame.Rect(0,0,25,25)

        # velocity_x formulas
        self.x += self.velocity_x
        #self.y += self.velocity_y + constant_y
        self.y += self.velocity_y
        self.velocity_x *= 0.95
        self.velocity_y *= 0.9

        # collisions
        self.collision_rect.center = (960+(self.velocity_x*4), constant_y+100)
        #pygame.draw.rect(screen, self.collision_color, self.collision_rect)
        
        # idle animation
        elapsed_time = ((pygame.time.get_ticks() - self.time_last_move)) # timer start after last move
        if (self.actions[0] == Tcrouch) and (elapsed_time > self.inactive): # if tanjie is crouching, and timer is up, 
            self.actions[0] = (Tcrouch_idle) # transition back to idle animation
            self.actions.append(Tidle)

        # image divided by 2, on (x,y), marksk the center point
        center = (((WIDTH/2 - 250) + (self.velocity_x*4)), (self.velocity_y + constant_y - 125))
        if self.looking_left == True: screen.blit(self.actions[0], center) # looking left
        else: screen.blit(pygame.transform.flip(self.actions[0], True, False), center) # looking right
        #pygame.draw.circle(screen, RED, (WIDTH/2, constant_y), 5) # debug circle


class Environment:
    def __init__(self, image:pygame.Surface, x, y, parralax:float=1):
        self.image = image
        self.x = x
        self.y = y
        self.parralax = parralax
        self.lightcooldown = 0

    def render(self, tanjie_x: float):
        finalpos_x = ((self.x + tanjie_x) * self.parralax)
        screen.blit (self.image, (finalpos_x, self.y))
        
    def renderpostlight(self, tanjie_x: float):
        chance = random.randint(1,1000)
        if chance == 1: self.lightcooldown = 100
        else: self.lightcooldown -= 1
        if self.lightcooldown <= 0:
            finalpos_x = ((self.x + tanjie_x) * self.parralax)
            screen.blit (LampLight, (finalpos_x, self.y))


class Border:
    def __init__(self):
        self.newbordersize = 300
        self.bordersize = 1900
        self.border1 = pygame.Rect(0,0,1920,self.bordersize)
        self.border2 = pygame.Rect(0,1081-self.bordersize,1920,self.bordersize)
        
    def render(self, gamerunning: bool):
        self.bordersize = pygame.math.lerp(self.bordersize, self.newbordersize, .1)
        self.border1 = pygame.Rect(0,0,1920,self.bordersize)
        self.border2 = pygame.Rect(0,1081-self.bordersize,1920,self.bordersize)
        pygame.draw.rect(screen, BLACK, self.border1)
        pygame.draw.rect(screen, BLACK, self.border2)

        if gamerunning == False:
            screen.blit(Menu, (1360 - (Menu.get_width()/2), (780 -self.bordersize)))
            screen.blit(FNWT_Logo, (560 - (FNWT_Logo.get_width()/2), self.bordersize))
    
    def changebordersize(self, value):
        self.newbordersize = value


#def debugging( tanjie, score):
    #score_text = font.render(f'Score: {score}', True, GREEN)
    #screen.blit(score_text, (10, 10))
    #debug1 = font.render(f'invulnerable: {(tanjie.invulnerable)}', True, GREEN)
    #screen.blit(debug1, (10, 70))
    
    #debug2 = font.render(f'looking left: {(tanjie.looking_left)}', True, GREEN)
    #screen.blit(debug2, (10, 100))
    
    #debug3 = font.render(f'tanjie velocity_x: {round(tanjie.velocity_x,1)}', True, GREEN)
    #screen.blit(debug3, (10, 130))
    #debug4 = font.render(f'tanjie velocity_y: {round(tanjie.velocity_y,1)}', True, GREEN)
    #screen.blit(debug4, (10, 160))
    #debug5 = font.render(f'tanjie free jump: {round(tanjie.freejump,1)}', True, GREEN)
    #screen.blit(debug5, (10, 190))

# main
def main():
    ticks = pygame.time.get_ticks()
    tanjie = Player()
    border = Border()
    enemies = [] #must be enemy class
    score = 0
    spawn_counter = 0
    game_started = False
    BG = []
    for x in range(10):
        imagex = random.randint(-10000,10000)
        imagey = 0
        image = LampPost
        parralax = -1
        BG.append(Environment(image, imagex, imagey, parralax))
    FG = []
    for x in range(50):
        imagex = random.randint(-10000,10000)
        randomimage = random.choice([FG1, FG2, FG3])
        if randomimage == FG1: imagey = 0
        elif randomimage == FG2: imagey = 1080 - 200
        elif randomimage == FG3: imagey = 1080 - 200
        parralax = random.randint(-4,-2)
        FG.append(Environment(randomimage, imagex, imagey, parralax))
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_LEFT: tanjie.move("left")
                elif event.key == pygame.K_RIGHT: tanjie.move("right")
                game_started = True

        # calculate elapsed time
            elapsed_seconds = (pygame.time.get_ticks() - ticks) // 1000
            if elapsed_seconds >  total_game_seconds:
                break # stops the game

        # calculate game time
            game_hour, game_minute, = get_time(elapsed_seconds)

        # format time for display
            if game_hour >= end_time:
                break
                # stops the game
            time_string = time_format(game_hour,game_minute)

       
        # enemies
        if game_started == True:
            border.changebordersize(0)
            spawn_counter += 1
            if spawn_counter >= ENEMY_SPAWN_RATE:
                enemies.append(Enemy(tanjie))
                spawn_counter = 0
            for enemy in enemies:
                enemy.move()

        # drawing
        screen.fill(WHITE) #debug white screen
        screen.blit(Street, (0,0)) #draw street
         # render time
        clock_text = font.render(time_string, True, WHITE)
        screen.blit(clock_text, (875,10))
        
        screen.blit(Menu, (600 - tanjie.x, 780)) # draw menu
        
        for x in BG: x.render(tanjie.x + tanjie.velocity_x) # spawn Background lamp posts
        tanjie.draw() # draw tanjie
        for enemy in enemies: enemy.draw(tanjie)
        for x in BG: x.renderpostlight(tanjie.x + tanjie.velocity_x) # spawn lamp light
        for x in FG: x.render(tanjie.x) # spawn Foreground

        # collisions
        for enemy in enemies:
            if tanjie.collision_rect.colliderect(enemy.collision_rect):
                tanjie.collide(enemy.x)
                enemies.remove(enemy)
                tanjie.collision_color = GREEN
            else: tanjie.collision_color = WHITE

        
        
        border.render(game_started)
        
        # debugging
        #debugging(tanjie, score)
        
        
        pygame.display.flip()
        clock.tick(FPS)
        

# start game
main()