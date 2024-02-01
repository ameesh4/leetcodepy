class Solution:
    def intToRoman(self, num: int) -> str:
        out = ''
        intdict = {1: "I", 5: "V", 10: "X",50: "L", 100: "C", 500: "D", 1000: "M"}
        m = int(num/1000)
        num = num - 1000 * m
        out += intdict[1000] * m
        c = int(num/100)
        temp = ''
        if c == 4:
            temp = "CD"
        elif c < 5:
            temp = intdict[100] * c
        elif c == 5:
            temp = intdict[500]
        elif c == 9:
            temp = "CM"
        else:
            temp = "D" + intdict[100] * (c-5)

        out += temp

        num = num - 100 * c
        x = int(num/10)
        if x == 4:
            temp = "XL"
        elif x < 5:
            temp = intdict[10] * x
        elif x == 5:
            temp = intdict[50]
        elif x == 9:
            temp = "XC"
        else:
            temp = "L" + intdict[10] * (x-5)

        out += temp
        num = num - 10 * x

        if num == 4:
            temp = "IV"
        elif num < 5:
            temp = intdict[1] * num
        elif num == 5:
            temp = intdict[5]
        elif num == 9:
            temp = "IX"
        else:
            temp = "V" + intdict[1] * (num-5)

        out += temp
        return out
    
def main():
    print(Solution().intToRoman(60))

main()


