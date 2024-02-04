class Solution:
    def __init__(self):
        self.move = [0, 0]
        self.record = []
        self.current_direction = "N"
    
    def isRobotBounded(self, instructions: str) -> bool:
        self.record.append(self.move[:])
        while len(self.record) < 1:
            for a in instructions:
                if a == "G":
                    self.moveForward(self.current_direction)
                    self.record.append(self.move[:])
                elif a == "L":
                    self.current_direction = self.turnLeft(self.current_direction)
                elif a == "R":
                    self.current_direction = self.turnRight(self.current_direction)

        if self.record[-1] == [0, 0]:
            return True
        else:
            return False
                
            

    def moveForward(self, direction: str) -> None:
        if direction == "N":
            self.move[1] += 1
        elif direction == "S":
            self.move[1] -= 1
        elif direction == "E":
            self.move[0] += 1
        else:
            self.move[0] -= 1

    def turnLeft(self, direction: str) -> str:
        if direction == "N":
            return "W"
        elif direction == "W":
            return "S"
        elif direction == "S":
            return "E"
        else:
            return "N"
        
    def turnRight(self, direction: str) -> str:
        if direction == "N":
            return "E"
        elif direction == "E":
            return "S"
        elif direction == "S":
            return "W"
        else:
            return "N"
        
def main():
    print(Solution().isRobotBounded("LRRRRLLLRL"))

if __name__ == "__main__":
    main()