class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if (arr[i + 1] - arr[i]) == diff:
                continue
            else:
                return False

        return True
            

def main():
    print(Solution().canMakeArithmeticProgression([1,2,4]))

main()