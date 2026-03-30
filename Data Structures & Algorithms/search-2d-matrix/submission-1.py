class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            elif target >= matrix[mid][0] and target <= matrix[mid][-1]: # could b else
                left2 = 0
                right2 = len(matrix[mid]) - 1

                while left2 <= right2:
                    inner_mid = (left2 + right2) // 2

                    if target < matrix[mid][inner_mid]:
                        right2 = inner_mid - 1
                    elif target > matrix[mid][inner_mid]:
                        left2 = inner_mid + 1
                    elif target == matrix[mid][inner_mid]:
                        return True
                return False
        return False