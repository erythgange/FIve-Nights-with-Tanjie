import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
FPS = 60 
ENEMY_SPAWN_RATE = 30  # Lower is faster
ENEMY_HIT_RADIUS = 50

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the displaya
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("One Finger Death Punch - Simplified")

# Load assets
font = pygame.font.Font(None, 36)

# Enemy class
class Enemy:
    def __init__(self):
        self.x = random.choice([0, WIDTH])
        self.y = random.randint(100, HEIGHT - 100)
        self.direction = 1 if self.x == 0 else -1
        self.speed = 5

    def move(self):
        self.x += self.speed * self.direction

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), 20)

    def is_hit(self, pos):
        return (pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2 < ENEMY_HIT_RADIUS ** 2

# Main game loop
def main():
    clock = pygame.time.Clock()
    enemies = []
    score = 0
    spawn_counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for enemy in enemies:
                    if enemy.is_hit(mouse_pos):
                        enemies.remove(enemy)
                        score += 1
                        break

        # Spawn enemies
        spawn_counter += 1
        if spawn_counter >= ENEMY_SPAWN_RATE:
            enemies.append(Enemy())
            spawn_counter = 0

        # Move enemies
        for enemy in enemies:
            enemy.move()

        # Remove off-screen enemies
        enemies = [enemy for enemy in enemies if 0 < enemy.x < WIDTH]

        # Drawing
        screen.fill(WHITE)
        for enemy in enemies:
            enemy.draw()

        # Draw score
        score_text = font.render(f'Score: {score}', True, GREEN)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()