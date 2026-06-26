numbers = {"a": 40, "b":60,"c":80, "d": 90, "f": 100}
abover = {key: value for key, value in numbers.items() if value > 50} 
print(abover)