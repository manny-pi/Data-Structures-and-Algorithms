import pygame 
import pygame.mouse as mouse 
from pygame.time import Clock
from random import randint as r

from sys import path 
path.append("/Users/Omani/Desktop/Personal/Education/Computer Science/Python/Python Projects/Algorithms/visualizers/visualizers")
from bar import Bar 


def test_bar(data_set=None): 
    pygame.init() 

    if data_set == None: 
        data_set = [r(0, 100) for i in range(10)]

    # Set game dimensions 
    WIDTH, HEIGHT = 1000, 400
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), display=0)
    pygame.display.set_caption("Algorithm Visualizer")

    # Animation clock 
    clock = Clock() 
    FRAMES_PER_SECOND = 10

    # Create a bar to test 
    init_x, init_y = 0, 0
    width = int( (1 / len(data_set) ) * WIDTH )
    height = HEIGHT

    opacity = 255 
    bar = Bar(init_x, init_y, width, height, (255, 75, 75, opacity))

    running = True 
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            
            # Execute if the mouse was left clicked 
            if mouse.get_pressed()[0] == 1: 
                x, y = r(0, WIDTH-bar.width), r(0, HEIGHT-bar.height)
                print(" - - - - move object - - - - ")  
                bar.set_position(x, y)
                print(bar)

        # Clear the window 
        # - - - - - - - - - -   
        WINDOW.fill((255, 255, 255))        

        # Draw the graphics 
        # - - - - - - - - - -
        WINDOW.blit(bar.surface, (bar.x, bar.y))

        # Update the frame 
        # - - - - - - - - - -
        pygame.display.flip() 

        # - - - - - - - - - - 
        clock.tick(FRAMES_PER_SECOND)


if __name__ == "__main__": 
    test_bar()