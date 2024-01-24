class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sl = list(s)
        tl = list(t)

        for i in t:
            if i in sl:
                sl.remove(i)
                tl.remove(i)

        print(''.join(tl))

def main():
    sol = Solution()
    print(sol.findTheDifference("abcdef", "abbccddeef"))

main()