class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows = len(matrix)
        columns = len(matrix[0])
        
        new_matrix = [ [0 for i in range(rows)] for i in range(columns)]
        for row in range(rows):
            for column in range(columns):
                new_matrix[column][row] = matrix[row][column]
         
                
        return new_matrix
