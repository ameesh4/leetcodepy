class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = self.binaryToDecimal(a) + self.binaryToDecimal(b)
        if self.decimalToBinary(sum) == "":
            return "0"
        else:
            return self.decimalToBinary(sum)
    
    def binaryToDecimal(self, a: str):
        sum = 0
        b = len(a) - 1
        for i in a:
            sum = sum + (int(i) * (2**b))
            b -= 1
        
        return sum
    
    def decimalToBinary(self, a: int):
        res = ""
        while a > 0:
            res = str(a % 2) + res
            a = a // 2
        
        return res

def main():
    sol = Solution()
    # print(sol.addBinary("11", "1"))
    print(sol.binaryToDecimal("0"))
    print(sol.decimalToBinary(0))

if __name__ == "__main__":
    main()