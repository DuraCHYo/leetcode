from itertools import count


def is_armstrong_number(number):
    num = list(str(number))
    result = 0
    for i in num:
        result += int(i) ** len(num)
    if number == result:
        return True
    else:
        return False

if __name__ == '__main__':
    a = is_armstrong_number(5)
    print(a)