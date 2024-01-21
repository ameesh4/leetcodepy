class Solution:
    def unique_occurences(self, arr: list[int]) -> bool:
        intdict = {}
        for a in arr:
            if a in intdict:
                intdict[a] = intdict[a] + 1
            else:
                intdict[a] = 1
            
        intdict = dict(sorted(intdict.items()))
        b = 0
        values = list(intdict.values())
        for a in  values:
            b = 0
            for key in intdict:
                if a == intdict[key]:
                    b += 1

            if b > 1:
                return False
            else:
                continue

        return True


def main():
    arr = [1, 5, 4, 5, 1, 1, 2, 2, 2, 2]
    sol = Solution()
    print(sol.unique_occurences(arr))

if __name__ == "__main__":
    main()

            
