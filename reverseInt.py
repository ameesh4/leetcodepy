class Solution:
    def reverse(self, x: int) -> int:
        temp = str(x)
        res = ''
        if temp[0] == "-":
            temp = list(temp)
            temp.pop(0)
            temp = "".join(temp)
            res = '-' + temp[::-1]
        else:
            res = temp[::-1]
            
        res = int(res)
        if res > -pow(2, 31) and res < pow(2, 31) - 1:
            return res
        else:
            return 0 

def main():
    print(Solution().reverse(-9018239011))

main()