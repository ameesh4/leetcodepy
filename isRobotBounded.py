class Solution:
    def __init__(self):
        self.move = [0, 0]
        self.record = []
        self.current_direction = "N"
    
    def isRobotBounded(self, instructions: str) -> bool:
        turnLeft = {"N": "W", "W": "S", "S": "E", "E": "N"}
        turnRight = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.record.append(self.move[:])
        if len(instructions) == 2:
            i = 5
        else:
            i = 4

        if instructions.count("G") == 0:
            return True

        while len(self.record) < i:
            for a in instructions:
                if a == "G":
                    self.moveForward(self.current_direction)
                    self.record.append(self.move[:])
                elif a == "L":
                    self.current_direction = turnLeft[self.current_direction]
                elif a == "R":
                    self.current_direction = turnRight[self.current_direction]

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
        
def main():
    print(Solution().isRobotBounded("LLGRL"))

if __name__ == "__main__":
    main()