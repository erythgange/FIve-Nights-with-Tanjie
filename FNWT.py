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
Tidle = pygame.image.load('FNWT/Assets/Tidle.png').convert_alpha()
BG = pygame.image.load('FNWT/Assets/BG.png').convert()
RAT = pygame.image.load('FNWT/Assets/Ridle.png').convert_alpha()












# class enemy
class Enemy:
    def __init__(self):
        self.x = random.choice([0, WIDTH])
        self.y = 550
        self.direction = 1 if self.x == 0 else -1
        self.speed = 10

    def move(self): self.x += self.speed * self.direction
    def draw(self): 
        center = (self.x - (RAT.get_width()/2), self.y - (RAT.get_height()/2))
        if self.direction == -1: screen.blit(pygame.transform.flip(RAT, True, False), center)
        else: screen.blit(RAT, center)
        
        pygame.draw.circle(screen, RED, (self.x, self.y), 5) # debug circle
        
    def is_hit(self, pos): return (pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2 < ENEMY_HIT_RADIUS ** 2

# class player
class Player:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = 550
    

        self.can_attack = True
        self.looking_left = True 

    def move(self, direction:str):
        if direction == "left": 
            self.x = self.x - 200
            self.looking_left = True
        if direction == "right": 
            self.x = self.x + 200
            self.looking_left = False

    def draw(self):
        center = (self.x - (Tidle.get_width()/2), self.y - (Tidle.get_height()/2))
        if self.looking_left == True: screen.blit(CAT, center)
        else: screen.blit(pygame.transform.flip(CAT, True, False), center)
        pygame.draw.circle(screen, RED, (self.x, self.y), 5) # debug circle

    def is_hit(self): pass











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
            if event.type == pygame.KEYDOWN and tanjie.can_attack == True:
                if event.key == pygame.K_LEFT: tanjie.move("left")
                if event.key == pygame.K_RIGHT: tanjie.move("right")

                mouse_pos = pygame.mouse.get_pos()
                for enemy in enemies:
                    if enemy.is_hit(mouse_pos):
                        enemies.remove(enemy)
                        score += 1
                        break
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
        clock.tick(FPS)

# start game
main()