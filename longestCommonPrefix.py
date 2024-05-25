class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        elif strs.count(strs[0]) == len(strs):
            return strs[0]
        elif strs[0] == "":
            return ""
        
        prefix = strs[0][0]
        i = 0
        j = 1
        res = ""
        while i < len(strs):
            if prefix == strs[i][0:j]:
                i += 1
            elif j >= len(strs):
                # prefix = prefix.replace(prefix[-1], "", 1)
                res = prefix[0:j-1]
                break
            elif prefix != strs[i][0:j]:
                # prefix = prefix.replace(prefix[-1], "", 1)
                res = prefix[0:j-1]
                break
                
            if i == len(strs):
                i = 0
                j += 1
                try:
                    prefix = prefix + strs[0][j-1]
                except IndexError:
                    res = prefix
                    break

        return res

def main():
    sol = Solution()
    print(sol.longestCommonPrefix(["abab","aba","abc"]))

main()