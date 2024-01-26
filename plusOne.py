class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        b = ''
        c = []
        for a in digits:
            b = b + str(a)

        b = int(b)
        b += 1
        b =  str(b)
        b = list(b)
        for d in b:
            c.append(int(d))

        return c


def main():
    print(Solution().plusOne([8, 9, 8, 9]))

main()