# create a class Solution with tictactoe method to check the winner of the game
class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        if len(moves) < 5:
            return "Pending"

        A = [[]]
        B = [[]]
        i = 0
        while i < len(moves):
            if i % 2 == 0:
                A.append(moves[i])
            else:
                B.append(moves[i])

            i += 1

        if self.winCases(A):
            return "A"
        elif self.winCases(B):
            return "B"
        else:
            if moves.length == 9:
                return "Draw"
            else:
                return "Pending"
            

    def winCases(self, moves: list[list[int]]) -> bool:
        for i in range(3):
            if moves.count([i, 0]) and moves.count([i, 1]) and moves.count([i, 2]):
                return True
            if moves.count([0, i]) and moves.count([1, i]) and moves.count([2, i]):
                return True
        if moves.count([0, 0]) and moves.count([1, 1]) and moves.count([2, 2]):
            return True
        if moves.count([0, 2]) and moves.count([1, 1]) and moves.count([2, 0]):
            return True
        
        return False
    
def main():
    print(Solution().tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))

if __name__ == "__main__":
    main()