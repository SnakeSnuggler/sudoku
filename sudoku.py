import numpy as np
import random as random

print("Hello World...") # changed to be less enthusiastic
for i in range(10):
	print("This is the "+str(i)+"th message!")

print("You found the end! Bye bye!")
for i in range (5):
    print("I am a genius my code is better")
exit() # very necessary, earth blows up if this isnt included




class SudokuBoard:
    def __init__(self) -> None:
        self.array = np.empty((9,9), dtype=int)
        
    def fill_random(self, n_squares):
        indices = np.arange(9)
        for _ in range(n_squares):
            if indices.size == 0:
                indices = np.arange(9)
            row = random.randint(0, indices.size)
            #add insertion func here
            #self.array(row, )
            
            indices = np.delete(indices, row)

    def check_valid_placement(self, number, row, col):
        pass
    
    #check for the 
    def check_square(self, number, row, col):
        square_row = row // 3
        square_col = col // 3
        
        square = self.array[square_row*3:square_row*3+3, square_col*3:square_col*3+3]
        
        return not np.isin(number,square)    
    
    def check_row(self, number, row):
        for j in range(self.array.shape[1]):
            if self.array[row,j] == number:
                return False
        return True       
    
    def check_col(self, number, col):
        for i in range(self.array.shape[0]):
            if self.array[i, col] == number:
                return False
        return True            
            
            
        
         
     