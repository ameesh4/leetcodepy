class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp = nums.copy()
        nums.clear()
        for i in range(len(temp)):
            if i == len(temp)-1:
                nums.append(temp[i])
            elif temp[i] != temp[i+1]:
                nums.append(temp[i])

        print(nums)
    
def main():
    sol = Solution()
    sol.removeDuplicates([1,1,2])

main()
