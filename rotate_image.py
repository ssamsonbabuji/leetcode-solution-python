class Solution:

  def rotate(self, matrix):

    n=len(matrix)

    m=len(matrix[0])

    for i in range(n):

      for j in range(i,m):

        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    for i in range(n):

      matrix[i].reverse()   

    return matrix
