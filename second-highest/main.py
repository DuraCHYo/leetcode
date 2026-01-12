class Solution:
    def secondHighest(self, s: str) -> int:
        digit = list(filter(str.isdigit, s))
        if max(digit) == min(digit):
            return int(-1)
        else:
            return int(digit[1])


print(Solution().secondHighest("dfa12321afd"))
