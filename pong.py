import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

paddle_x = 20
paddle_y = 225
paddle_width = 10
paddle_height = 150

cpu_x = 770
cpu_y = 225
cpu_width = 10
cpu_height = 150
cpu_speed = 10

ball_x = 400
ball_y = 300
ball_size = 15
ball_speed_x = 8
ball_speed_y = 8

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_y = paddle_y - 10
    if keys[pygame.K_DOWN]:
        paddle_y = paddle_y + 10
    if paddle_y < 0:
        paddle_y = 0
    if paddle_y > 450:
        paddle_y = 450

    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y

    if ball_y < 0:
        ball_speed_y = ball_speed_y * -1
    if ball_y > 600 - ball_size:
        ball_speed_y = ball_speed_y * -1

    if ball_x > 800 - ball_size:
        ball_x = 400
        ball_y = 300

    if ball_x < paddle_x + paddle_width and ball_y + ball_size > paddle_y and ball_y < paddle_y + paddle_height:
        ball_speed_x = ball_speed_x * -1
    if ball_x < 0:
        ball_x = 400
        ball_y = 300

    if ball_x + ball_size > cpu_x and ball_y + ball_size > cpu_y and ball_y < cpu_y + cpu_height:
        ball_speed_x = ball_speed_x * -1

    if ball_y < cpu_y:
        cpu_y = cpu_y - cpu_speed
    if ball_y > cpu_y:
        cpu_y = cpu_y + cpu_speed

    if cpu_y < 0:
        cpu_y = 0
    if cpu_y > 450:
        cpu_y = 450

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (cpu_x, cpu_y, cpu_width, cpu_height))
    pygame.draw.rect(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
