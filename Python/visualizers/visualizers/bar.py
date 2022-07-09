from pygame.sprite import Sprite 
from pygame import Surface 
from random import randint as r 


def hexToRGB(col: int): 
    """ Returns a tuple containing RGB color values """

    R = col >> 16 
    G = (col - (R << 16)) >> 8 
    B = col - ((col >> 8) << 8)

    return (R, G, B)
    

class Bar(Sprite):

    MAX_VALUE = 1

    def __init__(self, value=0, dim=(), bottomleft=()): 
        """ Initialize a Bar object with dimension W x H, and bottom lefft at (X, Y) """ 

        super().__init__() 

        self.value = value 
        self.bottomleft = bottomleft

        self.surface = Surface(dim) 
        self.rect = self.surface.get_rect(bottomleft=self.bottomleft) 

        color = int(0xFFFFFF * (value / Bar.MAX_VALUE))
        self.color = hexToRGB(color)
        self.surface.fill(self.color)


    def __lt__(self, other): 
        return self.value < other.value 

    def __le__(self, other): 
        return self.value <= other.value 

    def __gt__(self, other): 
        return self.value > other.value 

    def __ge__(self, other): 
        return self.value >= other.value 
    
    @classmethod    
    def setMax(cls, value: int): 
        """ Set the MAX_VALUE for the Bars. MAX_VALUE is used to determine the color intensity of each Bar """ 

        cls.MAX_VALUE = value 

