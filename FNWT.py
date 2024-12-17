import pygame
import random
import sys

# constants
pygame.init()
WIDTH, HEIGHT = 1920, 1080
FPS = 60 
ENEMY_SPAWN_RATE = 30  # Lower is faster
ENEMY_HIT_RADIUS = 50

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the displays
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Five Nights with Tanjie")

# assets
font = pygame.font.Font(None, 36)
CATimg = pygame.image.load('FNWT/Assets/TanjieSprites.png').convert_alpha()
CAT = pygame.transform.scale(CATimg, (250,250))
BG = pygame.image.load('FNWT/Assets/BG.png').convert()
RAT = pygame.image.load('FNWT/Assets/RAT.png').convert_alpha()

# Enemy class
class Enemy:
    def __init__(self):
        self.x = random.choice([0, WIDTH])
        self.y = 600
        self.direction = 1 if self.x == 0 else -1
        self.speed = 30

    def move(self): self.x += self.speed * self.direction
    def draw(self): pygame.draw.circle(screen, RED, (self.x, self.y), 20)
    def is_hit(self, pos): return (pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2 < ENEMY_HIT_RADIUS ** 2

# player
class Player:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = 500
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
        if self.looking_left == True:
            screen.blit(CAT, (self.x,self.y))
        else: screen.blit(pygame.transform.flip(CAT, True, False), (self.x,self.y))

    def is_hit(self): pass


# Main game loop
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
if __name__ == "__main__":
    main()