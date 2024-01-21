class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        print (matrix)
        n2 = len(matrix[0])

        r = n-2
        c = 0
        if r == -1:
            return min(matrix[0])

        for c in range(n2):
            if c == 0:
                arr = [matrix[r+1][c], matrix[r+1][c+1]]
                matrix[r][c] = matrix[r][c] + min(arr)
            elif c == n2-1:
                arr = [matrix[r+1][c], matrix[r+1][c-1]]
                matrix[r][c] = matrix[r][c] + min(arr)
            else:
                arr = [matrix[r + 1][c - 1], matrix[r+1][c+1], matrix[r+1][c]]
                matrix[r][c] += min(arr)

        matrix.pop(n-1)
        return self.minFallingPathSum(matrix)





def main():
    sol = Solution()
    arr = [[-19, 57, 18, 19], [-40,-5, 16, -20], [41, 32, 21, -41], [22, 33, 44, 55]]
    print(sol.minFallingPathSum(arr))

if __name__ == "__main__":
    main()