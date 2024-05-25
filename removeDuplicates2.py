class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp = nums.copy()
        nums.clear()
        for i in range(len(temp)):
            if i == len(temp)-1 or i + 1 == len(temp) or i + 2 == len(temp) or temp[i] != temp[i+1] or temp[i] != temp[i+2]:
                nums.append(temp[i])
            elif temp[i] == temp[i+1] and temp[i] != temp[i+2]:
                nums.append(temp[i])
                nums.append(temp[i])

        print(nums)
    
def main():
    sol = Solution()
    sol.removeDuplicates([0,0,1,1,1,1,2,3,3])

main()
