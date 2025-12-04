def encode(string):
    if not string:
        return ""

    result = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            if count == 1:
                result.append(string[i - 1])
            else:
                result.append(string[i - 1] + str(count))
            count = 1

    if count == 1:
        result.append(string[-1])
    else:
        result.append(string[-1] + str(count))

    return "".join(result)

string = input()

print(encode(string))