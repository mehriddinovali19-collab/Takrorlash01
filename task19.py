dict1 = {"olma":5}
dict2 = {"olma":3,"anor":2}

result = dict1.copy()

for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)
