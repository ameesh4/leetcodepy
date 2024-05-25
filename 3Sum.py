class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.subSets(nums, len(nums), 3, 0, [0]*3, 0, res)
        final = []
        for a in res:
            if sum(a) == 0:
                final.append(a)
        
        return final

    def subSets(self, arr, n, r,index, data, i, res):
        if(index == r):
            temp = data.copy()
            temp.sort()
            if temp not in res:
                res.append(temp)
            return
        
        if(i >= n):
            return
        
        data[index] = arr[i]
        self.subSets(arr, n, r,index + 1, data, i + 1, res)
        
        self.subSets(arr, n, r, index, data, i + 1, res)

def main():
    sol = Solution()
    print(sol.threeSum([-13,5,13,12,-2,-11,-1,12,-3,0,-3,-7,-7,-5,-3,-15,-2,14,14,13,6,-11,-11,5,-15,-14,5,-5,-2,0,3,-8,-10,-7,11,-5,-10,-5,-7,-6,2,5,3,2,7,7,3,-10,-2,2,-12,-11,-1,14,10,-9,-15,-8,-7,-9,7,3,-2,5,11,-13,-15,8,-3,-7,-12,7,5,-2,-6,-3,-10,4,2,-5,14,-3,-1,-10,-3,-14,-4,-3,-7,-4,3,8,14,9,-2,10,11,-10,-4,-15,-9,-1,-1,3,4,1,8,1]))

if __name__ == "__main__":
    main()