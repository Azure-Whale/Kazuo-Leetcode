matrix = [[0,1,0,0,2,0],
          [0,2,0,1,0,0],
          [1,1,0,0,0,0]]
# 0 free space, 1 box, 2 obstacle, rorate this matrix for k times, ratation will be done as 90 degree clock-wise
# the box will fall due to gravity.

# if you are rorating a matrix
# during every rotation
# the previous rows will become cols
# for example, if ROW, COL are the number of rows and cols of previous matrix respectively
# we will get:
# KEY1
# 行数会变成列，并且顺序反过来，所以行就变成了行-1-原先的行数
# 列数会变成行数且不变
# new_matrix[j][ROW - 1 - i] = matrix[i][j]
# KEY2
# Box下落会导致他的行数“增加”，并且落在障碍物或者矩阵底部，此时必须优先让最接近地面的box下落，不然会阻碍上方的box下落检测


class solution:
    def get_new_status(self,matrix,k):
        if k<=0:
            self.fall(matrix)
            return matrix
        while k:
            matrix = self.rotate(matrix)
            self.fall(matrix)
            k -= 1
        return matrix


    def fall(self,matrix):
        """
        iterate the whole matrix, once you find a 1, check if there are empty rooms below it, keep searching until you find the buttom
        Attention:
        1.There are obstacle, so the button could be either on top of obstacle or the buttom of the matrix
        2. you should iterate the matrix from back to start, you should guarantee that items which is cloest to the surface reach the surface firstly. Otherwise, you may meet
        this case. It's because the topest 1 find there has already been a 1 below it so it won't fall
        1
        1
        0
        0


        """
        print('execute falling func')
        ROW = len(matrix)
        COL = len(matrix[0])

        for row in range(ROW-1,-1,-1):
            for col in range(COL-1,-1,-1):
                if matrix[row][col] == 1:
                    current_row = row
                    update = False
                    while current_row+1 < ROW and matrix[current_row+1][col]==0:
                        current_row += 1
                        update = True
                    if update:
                        matrix[row][col] = 0
                        matrix[current_row][col] = 1
        self.show_matrix(matrix)

                    


    def rotate(self,matrix):
        """
        When you are rotating the matrix, the new coordinate follows the pattern that
        new_x = new_x
        """
        print('execute rotation')
        ROW = len(matrix)
        COL = len(matrix[0])
        new_matrix = [[0 for _ in range(ROW)] for _ in range(COL)]

        for i in range(ROW):
            for j in range(COL):
                new_matrix[j][ROW - 1 - i] = matrix[i][j]
        self.show_matrix(new_matrix)
        return new_matrix

    def show_matrix(self,matrix):
        for line in matrix:
            print(line)

case = solution()
print('START!!!!!')
M = case.get_new_status(matrix,3)