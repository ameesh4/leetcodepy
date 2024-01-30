class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        res = 0
        n = len(s)
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        try:
            while i < n:
                if m[s[i]] >= m[s[i+1]]:
                    res += m[s[i]]
                else:
                    res -= m[s[i]]

                i += 1

        except IndexError:
            res += m[s[i]]

        return res
            
def main():
    print(Solution().romanToInt("IX"))

main()
