import re

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        j = 1
        if len(s) <= 1:
            return False

        while j <= len(s)/2:
            k = len(s)/j
            temp: str = s[0:j] * int(k)
            if temp == s:
                return True
            else:
                j += 1

        return False
    
def main():
    sol = Solution()
    print(sol.repeatedSubstringPattern("abab"))

main()