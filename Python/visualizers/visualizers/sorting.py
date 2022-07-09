import pygame 
from pygame import Surface, time
from bar import Bar
from random import randint as r 

pygame.init() 


# Generate 1000 random values  
defaultData = [r(100, 1000) for i in range(200)] 


class Visualizer: 
    WIDTH, HEIGHT = 1000, 400
    MAIN_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    def __init__(self): 
        """ Initialize a visualizer object. Target is the Surface that the bars will be drawn to """

        self.__target = Visualizer.MAIN_WINDOW 

        self.__assignedDataset: list = None 
        self.__barSet: list = None

        self.__clock = time.Clock() 

    def assignDataset(self, dataset: list): 
        """ All algorithms will perform operations on this dataset unless otherwise is specified """ 

        self.assignedDataset = dataset
        self.barSet = self.__generateBars(self.assignedDataset)
        
    # ALGORITHMS 
    def selectionSort(self, dataset: list = None):
        """ Performs Selection Sort on the assigned dataset, or the argument """ 

        if dataset is None:
            barSet = self.__barSet 
        else: 
            barSet = self.__generateBars(dataset)
            self.__barSet = barSet

        running = True 
        j = 0
        tracker = 0
        while running: 
            
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    running = False 
                    break 

            while j < len(barSet) - 1:
                smallest = barSet[j]
                indexOfSmallest = j
                i = j + 1
                while i < len(barSet):
                    if barSet[i] < smallest:
                        smallest = barSet[i]
                        indexOfSmallest = i
                    i += 1

                current = barSet[j]
                barSet[j] = smallest
                barSet[indexOfSmallest] = current
                
                j += 1

                self.__updateFrame()

            tracker += 1

    def test_default(self): 
        """ Runs Selection Sort on the default data set """ 
        
        self.selectionSort(defaultData)

    def __generateBars(self, dataset: list) -> list: 
        """ Returns a list of Bar objects whose colors correspond with the values in the dataset """ 

        size = len(dataset)
        barWidth = self.__target.get_width() / size
        barHeight = self.__target.get_height() 
        Bar.setMax(max(dataset))

        j = 0 
        bars = list() 
        while j < size: 
            bar = Bar(value=dataset[j], dim=(barWidth, barHeight), bottomleft=(j * barWidth, barHeight))
            bars.append(bar)

            j += 1 

        return bars 

    def __updateFrame(self): 
        """ Updates the frames """

        for bar in self.__barSet: 
            self.__target.blit(bar.surface, bar.rect)
        pygame.display.flip() 

        self.__clock.tick(100)
        print("Rendering")
        

    @classmethod 
    def __end(cls): 
        """ Ends the program """
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return True 