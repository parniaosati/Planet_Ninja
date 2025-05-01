import pygame
import random
import math
from collections import deque

pygame.init()
pygame.mouse.set_visible(False)

# Screen setup
WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Ninja - White Trail Swipe")

# Load background
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Fruit names
fruit_names = ["apple", "banana", "watermelon", "grape", "pineapple"]
fruit_size = 160

# Load and scale fruit images
def load_image(name, sliced=False):
    if sliced:
        return pygame.transform.scale(pygame.image.load(name), (fruit_size // 2, fruit_size))
    return pygame.transform.scale(pygame.image.load(name), (fruit_size, fruit_size))

fruit_assets = {}
for name in fruit_names:
    fruit_assets[name] = {
        "whole": load_image(f"{name}.png"),
        "left": load_image(f"{name}_sliced_left.png", sliced=True),
        "right": load_image(f"{name}_sliced_right.png", sliced=True)
    }

# Font and colors
WHITE = (255, 255, 255)
font = pygame.font.SysFont('Arial', 24)

# Clock and physics
clock = pygame.time.Clock()
GRAVITY = 0.12
SPEED_SCALE = 0.7
max_flight_height = HEIGHT - fruit_size * 0.9
MAX_VY = -math.sqrt(2 * GRAVITY * max_flight_height)

# Swipe trail
trail_points = deque(maxlen=15)

# Sliced piece class
class SlicedPiece:
    def __init__(self, image, x, y, vx, vy, rotation_speed):
        self.image = image
        self.original_image = image
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.angle = 0
        self.rotation_speed = rotation_speed

    def update(self, dt):
        self.vy += GRAVITY * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.rotation_speed * dt
        self.image = pygame.transform.rotate(self.original_image, self.angle)

    def draw(self):
        rect = self.image.get_rect(center=(int(self.x), int(self.y)))
        screen.blit(self.image, rect)

    def expired(self):
        return self.y > HEIGHT + fruit_size

# Fruit class
class Fruit:
    def __init__(self):
        self.name = random.choice(fruit_names)
        self.image = fruit_assets[self.name]["whole"]
        self.original_image = self.image
        self.radius = fruit_size // 2
        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT + self.radius
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(MAX_VY * 0.95, MAX_VY)
        self.angle = 0
        self.rotation_speed = random.uniform(-4, 4)
        self.sliced = False

    def update(self, dt):
        self.vy += GRAVITY * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.angle += self.rotation_speed * dt
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        if self.x < self.radius:
            self.x = self.radius
            self.vx *= -1
        elif self.x > WIDTH - self.radius:
            self.x = WIDTH - self.radius
            self.vx *= -1

    def draw(self):
        rect = self.image.get_rect(center=(int(self.x), int(self.y)))
        screen.blit(self.image, rect)

    def is_near_mouse(self, mx, my, threshold=40):
        dist_sq = (self.x - mx) ** 2 + (self.y - my) ** 2
        return dist_sq <= threshold ** 2

    def expired(self):
        return self.y > HEIGHT + self.radius

    def slice(self):
        self.sliced = True
        pieces = []

        left = SlicedPiece(
            fruit_assets[self.name]["left"],
            self.x - 3,
            self.y,
            self.vx - 2,
            self.vy - 1,
            random.uniform(-5, -2)
        )
        right = SlicedPiece(
            fruit_assets[self.name]["right"],
            self.x + 3,
            self.y,
            self.vx + 2,
            self.vy - 1,
            random.uniform(2, 5)
        )
        pieces.extend([left, right])
        return pieces

# Game state
fruit = None
sliced_pieces = []
score = 0
running = True

while running:
    dt = clock.tick(60) / 16.67 * SPEED_SCALE
    screen.blit(background_image, (0, 0))

    mx, my = pygame.mouse.get_pos()
    trail_points.append((mx, my))  # Track trail

    if fruit is None:
        fruit = Fruit()

    if fruit and not fruit.sliced:
        fruit.update(dt)
        fruit.draw()
        if fruit.is_near_mouse(mx, my):
            sliced_pieces.extend(fruit.slice())
            fruit = None
            score += 1
        elif fruit.expired():
            fruit = None

    for piece in sliced_pieces:
        piece.update(dt)
        piece.draw()
    sliced_pieces = [p for p in sliced_pieces if not p.expired()]

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 🌀 Draw white meteor trail
    for i in range(len(trail_points) - 1):
        pos1 = trail_points[i]
        pos2 = trail_points[i + 1]
        width = max(4, int(16 * (1 - i / len(trail_points))))  # Thicker trail
        pygame.draw.line(screen, WHITE, pos1, pos2, width)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
