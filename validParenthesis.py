class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for a in s:
            if a == "(" or a == "{" or a == "[":
                stack.append(a)
            elif a == ")" and stack[-1] == "(":
                stack.pop(0)
            elif a == "}" and stack[-1] == "{":
                stack.pop(0)
            elif a == "]" and stack[-1] == "[":
                stack.pop(0)
        
        if stack == []:
            return True
        else:
            return False
        
def main():
    sol = Solution()
    print(sol.isValid("()[]"))

main()