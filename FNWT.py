import pygame
import random
import sys

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

# displays
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Five Nights with Tanjie")

# assets
font = pygame.font.Font(None, 36)
# Tanjie idle/crouch
Tidle = pygame.image.load('FNWT/Assets/Tidle.png').convert_alpha()
Tcrouch = pygame.image.load('FNWT/Assets/Tcrouch.png').convert_alpha()
Tidle_crouch = pygame.image.load('FNWT/Assets/Tidle-crouch.png').convert_alpha()
Tidle_crouchM = pygame.image.load('FNWT/Assets/Tidle-crouchM.png').convert_alpha()
Tcrouch_idle = pygame.image.load('FNWT/Assets/Tcrouch-idle.png').convert_alpha()
Tcrouch = pygame.image.load('FNWT/Assets/Tcrouch.png').convert_alpha()
Tcrouch_switch = pygame.image.load('FNWT/Assets/Tcrouch-switch.png').convert_alpha()
# Tanjie attack
Tcrouch_attacklong = pygame.image.load('FNWT/Assets/Tcrouch-attacklong.png').convert_alpha()
Tcrouch_attackshort = pygame.image.load('FNWT/Assets/Tcrouch-attackshort.png').convert_alpha()
Tattacklong_crouch = pygame.image.load('FNWT/Assets/Tattacklong-crouch.png').convert_alpha()
# Tanjie miss
Tattacklong_miss1 = pygame.image.load('FNWT/Assets/Tattacklong-miss1.png').convert_alpha()
Tattacklong_miss2 = pygame.image.load('FNWT/Assets/Tattacklong-miss2.png').convert_alpha()
Tattacklong_miss3 = pygame.image.load('FNWT/Assets/Tattacklong-miss3.png').convert_alpha()
Tattacklong_miss4 = pygame.image.load('FNWT/Assets/Tattacklong-miss4.png').convert_alpha()
Tmiss_crouchM = pygame.image.load('FNWT/Assets/Tmiss-crouchM.png').convert_alpha()
# Tanjie hit
Thit = pygame.image.load('FNWT/Assets/Thit.png').convert_alpha()
# Tanjie mirror frames
mirror_frames = [Tidle_crouchM, Tmiss_crouchM, Tcrouch_switch, Tattacklong_crouch]
# BG
Light = pygame.image.load('FNWT/Assets/Light.png').convert_alpha()
BG = pygame.image.load('FNWT/Assets/BG.png').convert()
Ridle = pygame.image.load('FNWT/Assets/Ridle.png').convert_alpha()



# constants
constant_y = 600






# class enemy
class Enemy:
    def __init__(self,tanjie_x):
        self.x = (random.choice([1000,-1000])) + 500 + tanjie_x
        #self.x = 0.00 + 500
        print(f"spawned enemy with self.x of: {round(self.x,1)}")
        #if spawned from tanjie's left:(self.x < tanjie_x), go right. vice versa
        if self.x < tanjie_x: self.direction = 1  
        else: self.direction = -1
        self.speed = 5

    def move(self): self.x += self.speed * self.direction
    def draw(self,tanjie_x): 
        
        finalx = (self.x - (tanjie_x)) + (Ridle.get_width()/2)
        #finalx = (self.x - (tanjie_x)) + (Ridle.get_width()/2) + 500
        finaly = constant_y - (Ridle.get_height()/2)
        
        center = (finalx, finaly)
        if self.direction == -1: screen.blit(pygame.transform.flip(Ridle, True, False), center)
        else: screen.blit(Ridle, center)
        
        pygame.draw.circle(screen, RED, (finalx + Ridle.get_width()/2, constant_y), 5) # debug circle
        
    def is_hit(self, pos): return (pos[0] - self.x) ** 2 + (pos[1] - constant_y) ** 2 < ENEMY_HIT_RADIUS ** 2

# class player
class Player:
    def __init__(self):
        
        # experiment variables (can change)
        self.framepause : int = 8 # how fast (ms) Tanjie moves every frame
        self.inactive : int = 1000 # how much time (ms) Tanjie returns to idle pose after moving
        self.speed : float = 30

        
        # constant variables (dont change)
        self.x : int = 0
        self.velocity : float = 0
        self.can_attack : bool = True
        self.looking_left : bool = True
        self.time_last_move : int = 0
        self.actions = [Tidle]
        self.frameduration = self.framepause

    def move(self, direction:str, keydown:bool = True):
        
        def attacklong():
                self.actions.append(Tcrouch_attacklong)
                self.actions.append(Tattacklong_crouch)
                self.actions.append(Tcrouch)

        if keydown == True and self.can_attack == True:
            self.can_attack = False # no spamming attack

            # from idle
            if self.actions[0] == (Tidle):
                if (direction == "left" and self.looking_left == True) or (direction == "right" and self.looking_left == False): 
                    self.actions.append(Tidle_crouch) # to crouch left
                if (direction == "right" and self.looking_left == True) or (direction == "left" and self.looking_left == False): 
                    self.actions.append(Tidle_crouchM) # to crouch right
                self.actions.append(Tcrouch) # hold crouch
                attacklong()
                
            # from crouch
            if self.actions[0] == Tcrouch:
                if (direction == "left" and self.looking_left == False) or (direction == "right" and self.looking_left == True):
                    self.actions.append(Tcrouch_switch) # if attacking behind, turn around first, then
                    self.actions.append(Tcrouch)
                attacklong() # long jumping attack

            # hitstop: pygame.time.delay(1000) # hitstop
    
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
        
            if self.actions[0] == Tcrouch_attacklong: # if jumping attack
                if self.looking_left == False: self.velocity = self.speed # going right
                else: self.velocity = -self.speed # going left
            if self.actions[0] == Tcrouch_attackshort:
                pass

        else: self.can_attack = True # if there is no appended action, tanjie can now attack

        # velocity formulas
        self.x += self.velocity
        self.velocity *= 0.9

        elapsed_time = ((pygame.time.get_ticks() - self.time_last_move)) # timer start after last move
        if (self.actions[0] == Tcrouch) and (elapsed_time > self.inactive): # if tanjie is crouching, and timer is up, 
            self.actions[0] = (Tcrouch_idle) # transition back to idle animation
            self.actions.append(Tidle)

        # image divided by 2, on (x,y), marksk the center point
        center = ((WIDTH/2 - self.actions[0].get_width()/2), constant_y - self.actions[0].get_height()/2)
        if self.looking_left == True: screen.blit(self.actions[0], center) # looking left
        else: screen.blit(pygame.transform.flip(self.actions[0], True, False), center) # looking right
        pygame.draw.circle(screen, RED, (WIDTH/2, constant_y), 5) # debug circle




# main
def main():
    clock = pygame.time.Clock()
    tanjie = Player()
    enemies = [] #must be enemy class
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
            enemies.append(Enemy(tanjie.x))
            spawn_counter = 0
        for enemy in enemies:
            enemy.move()

        # Remove off-screen enemies
        #enemies = [enemy for enemy in enemies if 0 < enemy.x < WIDTH]


        # drawing
        def cam_offset(inputpos, parralax=1):
            inputpos = (inputpos - tanjie.x) * parralax
            return inputpos
        
        bglocation = cam_offset(-4000)

        screen.fill(WHITE)
        screen.blit(BG, (bglocation, 1))
        tanjie.draw()
        for enemy in enemies: enemy.draw(tanjie.x)
        

        # debugging
        score_text = font.render(f'Score: {score}', True, GREEN)
        screen.blit(score_text, (10, 10))
        
        clock.tick(FPS)
        fps_text = font.render(f'FPS: {round(clock.get_fps())}', True, GREEN)
        screen.blit(fps_text, (10, 40))
        
        debug1 = font.render(f'tanjie_x: {round(tanjie.x,1)}', True, GREEN)
        screen.blit(debug1, (10, 70))
        
        debug2 = font.render(f'bg location: {round(bglocation,1)}', True, GREEN)
        screen.blit(debug2, (10, 100))
        
        debug3 = font.render(f'tanjie velocity: {round(tanjie.velocity,1)}', True, GREEN)
        screen.blit(debug3, (10, 130))
        
        
        pygame.display.flip()
        
# start game
main()