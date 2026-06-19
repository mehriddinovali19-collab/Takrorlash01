def numbers(numbers1, numbers2, operation ):
    if operation == "+":
        return numbers1 + numbers2
    elif operation == "-":
        return numbers1 - numbers2
    elif operation == "*":
        return numbers1 * numbers2
    elif operation == "/":
        if numbers2 == 0:
            print("You cannot divide to Zero!")
        return numbers1 / numbers2
    

def main():
    while True:
        numbers1 = float(input("Enter a frist number: "))
        numbers2 = float(input("Enter a second number: "))
        operation = input("Choose on of these opertaions: /, *, -, +: ")

        result = numbers(numbers1, numbers2, operation)
        print(f"Result: {result}")
        print("----------------------------------")

main()