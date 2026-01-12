class Solution:
    def maxPower(self, s: str) -> int:
        current_lenght = 1  # первый символ уже имеет длину 1
        max_lenght = 1  # минимальная максимальная длина - 1

        for index, letter in enumerate(s):
            if index > 0:  # избегаем s[-1] для первого символа
                if letter == s[index - 1]:
                    # продолжаем последовательность
                    current_lenght += 1  # просто +1
                    # обновляем максимум если нужно
                    if current_lenght > max_lenght:
                        max_lenght = current_lenght
                else:
                    # начинаем новую последовательность
                    current_lenght = 1  # начинаем с текущего символа

        return max_lenght


if __name__ == "__main__":
    print(Solution().maxPower("leetcode"))
