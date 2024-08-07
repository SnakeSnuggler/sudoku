import numpy as np
import random

class SudokuBoard:
    def __init__(self):
        self.array = np.empty((9,9), dtype=int)
        
    def fill_random(self, n_squares):
        indices = np.arange(9)
        for _ in range(n_squares):
            if indices.size == 0:
                indices = np.arange(9)
            
            print(f"before indices = {indices}")

            row = random.randint(0, indices.size)
            #add insertion func here
            #self.array(row, )
            
            indices = np.delete(indices, row)

            print(f"after indices = {indices}, chosen row = {row}")
            number_to_insert = random.randint(1,10)

    def check_valid_placement(self, number, row, col):
        return self.check_square(number,row,col) and self.check_row(number,row) and self.check_col(nubmer,col)

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
            
if __name__ == "__main__":
	test_board = SudokuBoard()
	test_board.board[3,4] = 5
	print(test_board.check_row(5, 3))
	print(test_board.check_row(5, 4))

	print(test_board.check_col(5, 3))
	print(test_board.check_col(5, 4))

	print(test_board.check_square(5, 3 ,4))
	print(test_board.check_square(5, 1 ,1))
	print(test_board.check_square(5, 4 ,4))
	print(test_board.check_square(5, 8 ,7))

     
