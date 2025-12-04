import os.path as p

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        u = p.commonprefix(strs)
        return u
strs = ["flower","flow","flight"]
qwe = Solution().longestCommonPrefix(strs)
print(qwe)
