class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0][0]
        i = 0
        j = 1
        res = ""
        while i < len(strs):
            if prefix == strs[i][0:j]:
                i += 1
            else:
                break
            
            if i == len(strs):
                i = 0
                j += 1
                res = prefix
                prefix = prefix + strs[0][j-1]

        return res

def main():
    sol = Solution()
    print(sol.longestCommonPrefix(["dog"]))

main()