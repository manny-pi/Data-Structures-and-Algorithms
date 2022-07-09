from sys import path 
path.append("/Users/Omani/Desktop/Personal/Education/Computer Science/Python/Python Projects/Algorithms/visualizers/visualizers")

import pygame 
import pygame.mouse as mouse 
from pygame.color import Color 
from pygame.surface import Surface
from pygame.time import Clock
from bar import Bar 
from random import randint as r 

def test_multiple_bars(data_set=None): 
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

    # Create Bars
    init_x, init_y = 0, 0                            # intial Coordinates of the Bar                 
    bar_width = int( (1 / len(data_set) ) * WIDTH )  # width of the Bar 
    bar_height = HEIGHT                              # height of the bar 
    bar_opacity = 0                                  # initial opacity 
    delta_opacity = (255/len(data_set))              # rate of change of opacity
    bars = []                                        # array of Bars
    for i in range(len(data_set)):                   
        bar = Bar(init_x, init_y, bar_width, bar_height, (59, 40, 16, bar_opacity))
        bars.append(bar)
        init_x += bar_width 
        bar_opacity += delta_opacity

        print(bar)
    
    # Animation loop 
    running = True 
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 

        # Clear the window 
        # - - - - - - - - - -   
        WINDOW.fill((255, 255, 255))        

        # Draw the Bars 
        # - - - - - - - - - -
        for bar in bars: 
            WINDOW.blit(bar.surface, (bar.x, bar.y))

        # Update the frame 
        # - - - - - - - - - -
        pygame.display.flip() 

        # - - - - - - - - - - 
        clock.tick(FRAMES_PER_SECOND)


if __name__ == "__main__": 
    test_multiple_bars()