import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Single Player Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle setup
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 15
paddle = pygame.Rect(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 8

# Ball setup
BALL_SIZE = 20
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_SIZE, BALL_SIZE)
ball_speed_x = random.choice([-4, 4])
ball_speed_y = -4  # always start going up

# Clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# Score
score = 0

# Control mode
computer_play = False  # default: human plays

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_speed_x = random.choice([-4, 4])
    ball_speed_y = -4

def computer_control():
    """Simple AI: move paddle toward the ball's x position."""
    if paddle.centerx < ball.centerx:
        paddle.x += paddle_speed
    elif paddle.centerx > ball.centerx:
        paddle.x -= paddle_speed

    # Keep paddle inside screen
    if paddle.left < 0:
        paddle.left = 0
    if paddle.right > WIDTH:
        paddle.right = WIDTH

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Toggle computer mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                computer_play = not computer_play

    # Human controls (only if computer is OFF)
    if not computer_play:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += paddle_speed
    else:
        computer_control()

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Wall collisions
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    # Paddle collision
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y *= -1
        score += 1

    # Ball missed
    if ball.bottom >= HEIGHT:
        reset_ball()
        score = 0

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    score_text = font.render(str(score), True, WHITE)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))

    # Display control mode
    mode_text = font.render("CPU" if computer_play else "Player", True, WHITE)
    screen.blit(mode_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
