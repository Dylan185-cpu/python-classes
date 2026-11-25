import math
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Add more Sprites")
background = pygame.image.load("background.png")
playerImg = pygame.image.load("player.png")
enemyImg = pygame.image.load("enemy.png")
font = pygame.font.Font("freesansbold.ttf", 32)

# Player
playerX = 370
playerY = 380
playerX_change = 0
playerY_change = 0
score = 0

# TODO 1: Create 7 enemies
num_of_enemies = 7
enemyX = []
enemyY = []

for i in range(num_of_enemies):
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 400))


# TODO 2: Collision detection
def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance < 40


running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # TODO 3: Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5

        if event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0

    # TODO 4: Move player and keep inside window
    playerX += playerX_change
    playerY += playerY_change

    playerX = max(0, min(playerX, 736))
    playerY = max(0, min(playerY, 436))

    # TODO 5: Check collisions and draw enemies
    for i in range(num_of_enemies):
        if isCollision(playerX, playerY, enemyX[i], enemyY[i]):
            score += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 400)

        screen.blit(enemyImg, (enemyX[i], enemyY[i]))

    screen.blit(playerImg, (playerX, playerY))
    screen.blit(font.render("Score : " + str(score), True, (255, 255, 255)), (10, 10))

    pygame.display.update()

pygame.quit()