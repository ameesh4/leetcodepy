import copy

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        hello = copy.deepcopy(nums)
        hello.sort()
        if hello == nums:
            return True
        
        hello.sort(reverse=True)
        if hello == nums:
            return True
        
        return False
        
def main():
    print(Solution().isMonotonic([1,3,2]))

main()