# Your code here
def matrix_builder(num):
    matrix=[]
    for i in range(num):
        sub_matrix = []
        for j in range(num):
            sub_matrix.append(1)
        matrix.append(sub_matrix)
        sub_matrix = []
    return matrix
print(matrix_builder(3))