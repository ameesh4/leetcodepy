class Solution:
    def lengthOfLastWord(self, s:str) -> int:
        s = s.strip()
        if not s:
            return 0
        return len(s.split()[-1])


def main():
    print(Solution().lengthOfLastWord("Hello World"))

if __name__ == "__main__":
    main()