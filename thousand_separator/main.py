class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n)) > 3:
            list_of_numbers = list(str(n))
            list_of_numbers.insert(1, ".")
            return "".join(list_of_numbers)
        else:
            return str(n)


print(Solution().thousandSeparator(9987))
