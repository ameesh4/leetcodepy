class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        memo = {}
        for i in range(len(nums)):
            if target - nums[i] in memo:
                return [memo[target-nums[i]], i]
            
            memo[nums[i]] = i
    
def main():
    arr = [2, 7, 11, 5]
    sol = Solution()
    print(sol.two_sum(arr, 16))

main()
