class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
    
def main():
    print(Solution().judgeCircle("UDLR"))
    print(Solution().judgeCircle("LL"))

if __name__ == "__main__":
    main()
