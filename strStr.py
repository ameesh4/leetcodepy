class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(haystack)
        b = len(needle)
        i = 0
        while i < a:
            if b == 1 and haystack[i] == needle:
                return i
            elif haystack[i:i+b] == needle:
                return i
            
            i += 1

        return -1

def main():
    sol = Solution()
    print(sol.strStr("aaabc", "abc"))

main()