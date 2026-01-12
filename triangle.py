def equilateral(sides):
    for i in sides:
        if i == 0:
            raise ValueError("стороны не могут быть равны 0")
        else:
            return True if min(sides) == max(sides) else False
def isosceles(sides):
    for i in range(len(sides)):
        if sides[i] == sides[i+2]:
            return True
        else:
            return False

def scalene(sides):
    pass

if __name__ == '__main__':
    a = isosceles([3, 4, 4])
    print(a)