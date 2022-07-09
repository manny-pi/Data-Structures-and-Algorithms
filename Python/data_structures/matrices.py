from random import randint 


class Matrix: 

    def __init__(self, rows=0, cols=0, src=None, random=False, min=0, max=10):
        """ Creates an m by n matrix from a given system """
        

        if src is not None: 
            self.rows = len(src)
            self.cols = len(src[0])
        else: 
            self.rows = rows 
            self.cols = cols 

        self.shape = {'rows': self.rows, 'cols': self.cols}  

        self.system = []
        row = 0 
        while row < self.rows: 
            col = 0 
            self.system.append([])
            while col < self.cols: 
                # Create a matrix from source data 
                if src is not None: 
                    self.system[row].append(src[row][col])
                
                # Create a matrix with random values 
                elif random: 
                    self.system[row].append(randint(min, max))
                
                # Create a matrix with zeros 
                else: 
                    self.system[row].append(0)

                col += 1
            row += 1

    def put(self, value, row, col): 
        if row < 0 or row > self.rows or col < 0 or col > self.cols: 
            raise Exception("Illegal index")

        self.system[row][col] = value

    def scale_ip(self, factor): 
        row = 0
        while row < self.rows: 
            col = 0
            while col < self.cols: 
                self.system[row][col] *= factor
                col += 1
            row += 1 
    
    def transpose_ip(self): 
        pass 

    def multiple(self, other): 
            pass 

    def __add__(self, other): 
        if other.rows != self.rows or other.cols != self.cols: 
            raise Exception("Matrix dimensions are incompatible") 

        result = [] 
        row = 0
        while row < self.rows: 
            result.append([])
            col = 0 
            while col < self.cols: 
                result[row].append(self.system[row][col] + \
                    other.system[row][col])

                col += 1
            row += 1 

        return Matrix(src=result)        

    def __str__(self): 
        ret = '[\n'
        row = 0
        while row < self.rows:
            ret += str(self.system[row]) 
            if row != self.rows - 1: 
                ret += ',\n'

            row += 1 

        ret += '\n]'  
        return ret 



class Vector: 
    def __init__(self): 
        pass 
    

def main(): 
    A = Matrix(3, 3, random=True, max=100)
    B = Matrix(3, 3, random=True, min=-100, max=100)
    C = A + B
    print(A, "\n")
    print(B, "\n")
    print(C, "\n")

    C.scale_ip(.5)
    print(C)


if __name__ == '__main__': 
    main() 