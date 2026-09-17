class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        result=[]

        top=0
        left=0
        right=len(matrix[0])

        down=len(matrix)


        while left <right and top <down:


            for i in range(left,right):

                result.append(matrix[top][i])

            top+=1


            for i in range(top,down):

                result.append(matrix[i][right-1])

            right-=1


            if not (top<down and left <right):
                break

            for i in range(right-1,left-1,-1):

                result.append(matrix[down-1][i])

            down-=1


            for i in range(down-1,top-1,-1):
                result.append(matrix[i][left])

            left+=1

        return result



