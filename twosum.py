class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        a = []
        for i in range(len(nums)):
            temp = nums.copy()
            if target - temp.pop(i) in temp:
                a.append([target-nums[i], nums[i]])
            
        return a
    
def main():
    arr = [-1, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    sol = Solution()
    print(sol.two_sum(arr, 0))

main()
