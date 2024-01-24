class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = len(word1)
        b = len(word2)
        res = ""
        if a < b :
            i = 0
            while i < a:
                res = res + word1[i] + word2[i]
                i += 1

            res = res + word2[i:b]
        else:
            i = 0
            while i < b:
                res = res + word1[i] + word2[i]
                i += 1

            res = res + word1[i:a]

        return res
    
def main():
    sol = Solution()
    print(sol.mergeAlternately("ab", "pqrs"))

main()