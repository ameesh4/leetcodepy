class Solution:
    def calPoints(self, ops: list) -> int:
        stack = []
        for op in ops:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        
        return sum(stack)

def main():
    print(Solution().calPoints(["5","2","C","D","+"]))

if __name__ == "__main__":
    main()