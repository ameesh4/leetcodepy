import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        fx = (x/3)**2 - x
        x0 = x/3
        while True:
            x0 = x0 - fx/(2*x0)
            fx = (x0)**2 - x
            if abs(fx) < 0.1:
                break

        return math.floor(x0)
    
def main():
    sol = Solution()
    print(sol.mySqrt(1660267039))

if __name__ == "__main__":
    main()