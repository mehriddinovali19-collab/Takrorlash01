fibonaci_num = int(input("Enter a number: "))
for num in range(1, fibonaci_num + 1):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+ b
    print(f"The Fibonacci number {num} = {a}")
    