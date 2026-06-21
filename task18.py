def frequency(text: str):

    result = {}

    for item in text:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    
    return result

text = "Hello World"
print(frequency(text))

         
