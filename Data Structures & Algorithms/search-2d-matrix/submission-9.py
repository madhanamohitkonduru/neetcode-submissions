class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows= len(matrix)
        cols = len(matrix[0])
        prev, curr = -10001, -10001
        for i in range(rows):
            curr = matrix[i][cols-1]
            print(prev, target, curr)
            if prev<=target<=curr:
                break
            else:
                prev = curr

        print(i)
        for j in matrix[i]:
            if target == j:
                return True

        return False