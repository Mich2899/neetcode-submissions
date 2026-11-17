class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        dir = 1 #right: 1, down: 2, left: 3, up: 4
        r=0
        c=0

        result = []

        while(top<=bottom) and (left<=right):
            result.append(matrix[r][c])
            if dir == 1:
                if c<right:
                    c+=1
                else:
                    top+=1
                    dir=2
                    r=top
                    # c=right
            elif dir == 2:
                if r<bottom:
                    r+=1
                else:
                    right-=1
                    dir=3
                    # r=bottom
                    c=right
            elif dir == 3:
                if c>left:
                    c-=1
                else:
                    bottom-=1
                    dir=4
                    r=bottom
                    # c=left
            elif dir == 4:
                if r>top:
                    r-=1
                else:
                    left+=1
                    dir=1
                    # r=top
                    c=left

        return result

