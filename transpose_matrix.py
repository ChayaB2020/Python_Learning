# given a matrix of row=3 column=4, transpose it. ie. row=4 column=3
'''matrix = [
     [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

o/p should be matrix= [[1,5,9]
                        [2,6,10]
                        [3,7,11]
                        [4,8,12]]

'''
def transpose(matrix):
    return [[row[i] for row in matrix]for i in range(4)]

def transpose2(matrix):
    return list(zip(*matrix))

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
print(transpose(matrix))
print(transpose2(matrix))
