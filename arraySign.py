from numpy import prod

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product = prod(nums)
        return self.signFunc(product)

    def signFunc(self, x):
        if x < 0:
            return -1
        elif x > 0:
            return 1
        else:
            return 0
        
def main():
    print(Solution().arraySign([9,72,34,29,-49,-22,-77,-17,-66,-75,-44,-30,-24]))

main()
        