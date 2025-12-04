class Solution:

    def longestCommonPrefix(self, strs) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

task = Solution()
strs = ["flower","flow","flight"]
print(task.longestCommonPrefix(strs))