class Solution:
    def romanToInt(self, s: str,num: int=0) -> int:
      romanNumbersArray = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
      for i in range(len(s)):
          if i!=len(s)-1 and romanNumbersArray[s[i]] < romanNumbersArray[s[i+1]]:
            num += romanNumbersArray[s[i]] * -1
          else:
            num += romanNumbersArray[s[i]]

      return num
s='VI'
qwe = Solution().romanToInt(s)
print(qwe)