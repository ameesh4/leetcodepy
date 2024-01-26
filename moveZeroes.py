class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = nums.count(0)
        for _ in range(i):
            nums.pop(nums.index(0))
            nums.append(0)

        return nums
    

def main():
    a = [0, 0, 1]
    print(Solution().moveZeroes(a))
        

main()