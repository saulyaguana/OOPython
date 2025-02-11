# 1 - import packages
from pathlib import Path
import pygame
from pygame.locals import *
import sys

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = Path(__file__).resolve().parent

# build a path to the file in the images folder
path_to_ball = BASE_PATH / "Images/ball.png"

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4- Load assets: image(s), sound(s), etc.
ball_image = pygame.image.load(path_to_ball)
# 5- Initialize variables

# 6 - Loop forever
while True:
    
    # 7- Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BLACK)
    
    # 10 - Draw all window elements
    # draw ball at position 1-- across (x) and 200 down (y)
    window.blit(ball_image, (100, 200))
    
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)