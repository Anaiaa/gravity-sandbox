# Gravity Sandbox - Stage 1: a ball that falls and bounces
#
# Setup (one time):   pip install pygame
# Click anywhere in the window to drop the ball from that spot.

import pygame

pygame.init()

# ---------- Settings you can play with ----------
WIDTH, HEIGHT = 800, 600
GRAVITY = 900.0   # pixels per second, every second (this is acceleration)
BOUNCE = 1.0      # 1.0 = perfect bounce, 0.0 = thuds and stays put
RADIUS = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Sandbox - Stage 1")
clock = pygame.time.Clock()

# ---------- The ball's state ----------
x, y = 400.0, 100.0
vx, vy = 0.0, 0.0

running = True
while running:
    # dt = how many seconds passed since the last frame (about 1/60)
    dt = clock.tick(60) / 1000

    # ---- 1. Handle input ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos      # drop the ball where you clicked
            vx, vy = 0.0, 0.0

    # ---- 2. Update the physics ----
    # Acceleration changes velocity. Velocity changes position.
    vy += GRAVITY * dt
    x += vx * dt
    y += vy * dt

    # Hit the floor? (In pygame, y grows DOWNWARD, so the floor is y = HEIGHT)
    if y + RADIUS > HEIGHT:
        y = HEIGHT - RADIUS     # put the ball back on top of the floor
        vy = -vy * BOUNCE       # flip direction, lose some energy

    # ---- 3. Draw ----
    screen.fill((15, 15, 25))
    pygame.draw.circle(screen, (240, 200, 80), (int(x), int(y)), RADIUS)
    pygame.display.flip()

pygame.quit()