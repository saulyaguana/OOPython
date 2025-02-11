# 1 - import packages
from pathlib import Path
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3
BASE_PATH = Path(__file__).resolve().parent

# build a path to the file in the images folder
path_to_ball = BASE_PATH / "Images/ball.png"
path_to_target = BASE_PATH / "Images/target.jpg"

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4- Load assets: image(s), sound(s), etc.
ball_image = pygame.image.load(path_to_ball)
target_image = pygame.image.load(path_to_target)

# 5- Initialize variables
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)   
target_rect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# 6 - Loop forever
while True:
    
    # 7- Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_x -= N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ball_x += N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                ball_y -= N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ball_y += N_PIXELS_TO_MOVE
            
    # 8 - Do any "per frame" actions
    # Check if the ball is colliding with the target
    ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    
    if ball_rect.colliderect(target_rect):
        print("Ball is touching the target")
    
    # 9 - Clear the window
    window.fill(BLACK)
    
    # 10 - Draw all window elements
    # draw ball at position 1-- across (x) and 200 down (y)
    window.blit(target_image, (TARGET_X, TARGET_Y))  # Draw the target
    window.blit(ball_image, (ball_x, ball_y))  # Draw the ball
    
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)