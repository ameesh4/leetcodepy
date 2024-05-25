class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = 0
        if target in nums:
                return nums.index(target)
        
        if len(nums) == 1:
            if nums[0] < target:
                return 1
            else:
                return 0
        
        while i <= len(nums)-1:
            if nums[i] == target:
                return i
            elif nums[i] < target and nums[i+1] > target:
                return i + 1
            elif nums[-1] < target:
                return len(nums)
            elif nums[0] > target:
                return 0
            
            
            i+=1
        
def main():
    sol = Solution()
    print(sol.searchInsert([1], 2))
    
main()