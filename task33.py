for num in range(1, 11):
    num_factorial = 1
    for i in range(1, num + 1):
        num_factorial *= i
    print(f"The factorial {num}! = {num_factorial}")
