# TODO: реализуйте функцию encode
def encode(string):
    count = 1
    result = []
    for i in range(count, len(string)):
        if i!=len(string)-1 and string[i] == string[i-1]:
            count += 1
        else:
            result += string[i-1]
            if count > 1:
                result += str(count)
            count = 1
    string = ''.join(result)
    return string

string = input()

print(encode(string))