def frequency(tple):
    result = {}

    for item in tple:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result

num = (1,2,2,3,3,3)
print(frequency(num)) 