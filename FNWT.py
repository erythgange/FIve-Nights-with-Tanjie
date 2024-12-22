import pygame
import random
import sys

# constants
pygame.init()
WIDTH, HEIGHT = 1920, 1080
FPS = 60 
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
# Tanjie 
Tidle = pygame.image.load('FNWT/Assets/Tidle.png').convert_alpha()
Tcrouch = pygame.image.load('FNWT/Assets/Tcrouch.png').convert_alpha()
Tidle_crouch = pygame.image.load('FNWT/Assets/Tidle-crouch.png').convert_alpha()
Tidle_crouchM = pygame.image.load('FNWT/Assets/Tidle-crouchM.png').convert_alpha()
pygame.transform.flip(Tidle_crouchM, True, False)
Tcrouch_idle = pygame.image.load('FNWT/Assets/Tcrouch-idle.png').convert_alpha()
Tcrouch = pygame.image.load('FNWT/Assets/Tcrouch.png').convert_alpha()
Tcrouch_switch = pygame.image.load('FNWT/Assets/Tcrouch-switch.png').convert_alpha()

Thit = pygame.image.load('FNWT/Assets/Thit.png').convert_alpha()



BG = pygame.image.load('FNWT/Assets/BG.png').convert()
Ridle = pygame.image.load('FNWT/Assets/Ridle.png').convert_alpha()












# class enemy
class Enemy:
    def __init__(self):
        self.x = random.choice([0, WIDTH])
        self.y = 550
        self.direction = 1 if self.x == 0 else -1
        self.speed = 10

    def move(self): self.x += self.speed * self.direction
    def draw(self): 
        center = (self.x - (Ridle.get_width()/2), self.y - (Ridle.get_height()/2))
        if self.direction == -1: screen.blit(pygame.transform.flip(Ridle, True, False), center)
        else: screen.blit(Ridle, center)
        
        pygame.draw.circle(screen, RED, (self.x, self.y), 5) # debug circle
        
    def is_hit(self, pos): return (pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2 < ENEMY_HIT_RADIUS ** 2

# class player
class Player:
    def __init__(self):
        
        # experiment variables (can change)
        self.framerate = 3
        
        # constant variables (dont change)
        self.x = WIDTH / 2
        self.y = 550
        self.can_attack = True
        self.looking_left = True
        self.frame = [Tidle]
        self.duration = self.framerate

    def move(self, direction:str, keydown:bool = True):
        if keydown == True:

            if self.frame[0] == Tidle:
                if direction == "left":        
                    self.frame.append(Tidle_crouch)
                    self.frame.append(Tcrouch)
                if direction == "right":        
                    self.frame.append(Tidle_crouchM)
                    self.frame.append(Tcrouch)

            if self.frame[0] == Tcrouch:
                self.frame.append(Tcrouch_switch)
                self.frame.append(Tcrouch)

            if direction == "left": 
                self.looking_left = True
            if direction == "right": 
                #self.x = self.x + 200
                self.looking_left = False
        


        else: # if keydown = false
            if direction == "left":
                pass

            if direction == "right": 
                pass
    
    def hit(self):
        x = self.current_sprite
        self.current_sprite = Thit
        pygame.time.delay(1000) # hitstop
        self.current_sprite = x

    def draw(self):
        
        # animation frame rate
        if len(self.frame) > 1:
            self.duration = self.duration - 1
            if self.duration == 0:
                self.frame.pop(0) # next animation
                self.duration = self.framerate # reset time

        center = (self.x - (self.frame[0].get_width()/2), self.y - (self.frame[0].get_height()/2)) # to center image
        if self.looking_left == True: screen.blit(self.frame[0], center) # looking left
        else: screen.blit(pygame.transform.flip(self.frame[0], True, False), center) # looking right
        pygame.draw.circle(screen, RED, (self.x, self.y), 5) # debug circle

    def is_hit(self): pass









def timer(time = float):
    time = time * 1000 # conversion from milisecond to second
    now = pygame.time.get_time()
    while True:
        if pygame.time.get_time() > (now + (time)): 
            return True

# main
def main():
    clock = pygame.time.Clock()
    tanjie = Player()
    enemies = []
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: tanjie.move("left", False)
                if event.key == pygame.K_RIGHT: tanjie.move("right", False)

        # enemies
        spawn_counter += 1
        if spawn_counter >= ENEMY_SPAWN_RATE:
            enemies.append(Enemy())
            spawn_counter = 0
            
        for enemy in enemies:
            enemy.move()

        # Remove off-screen enemies
        enemies = [enemy for enemy in enemies if 0 < enemy.x < WIDTH]

        # drawing
        screen.fill(WHITE)
        screen.blit(BG, (0,0))
        tanjie.draw()
        for enemy in enemies: enemy.draw()
        
        # draw score score and fps
        score_text = font.render(f'Score: {score}', True, GREEN)
        screen.blit(score_text, (10, 10))
        fps_text = font.render(f'FPS: {round(clock.get_fps())}', True, GREEN)
        screen.blit(fps_text, (10, 40))
        
        pygame.display.flip()
        
        # debug
        clock.tick(FPS)
        
        
# start game
main()