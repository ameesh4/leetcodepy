class Solution:
    def ThreeSum(self, nums: list) -> list:
        res = []
        i = 0
        while i < int(len(nums)/3):
            temp = nums.copy()
            a = 0 - temp[i]
            temp.pop(i)
            
            if(self.two_sum(temp, a)):
                data = self.two_sum(temp, a)
                for b in data:
                    b.append(nums[i])
                    b.sort()
                    if b not in res:
                        res.append(b)
            
            i += 1

        return res


    def two_sum(self, nums: list[int], target: int) -> list:
        a = []
        for i in range(len(nums)):
            temp = nums.copy()
            if target - temp.pop(i) in temp:
                a.append([target-nums[i], nums[i]])
            
        return a

def main():
    sol = Solution()
    nums = [0, 0, 0]
    print(sol.ThreeSum(nums))

main()
