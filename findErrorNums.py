class Solution:
    def findErrorNums(self, nums: list[int]):
        n = len(nums)
        i = 1
        checked = []
        while i <= n:
            if i in nums:
                checked.append(i)
            else:
                missing = i

            i += 1
                
        set1 = set(nums)
        set2 = set(checked)


        res = set1 - set2
            
        return [res, missing]



def main():
    nums = [1,2,2,4]
    print(Solution().findErrorNums(nums))

if __name__ == '__main__':
    main()


