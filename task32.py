numbers = []

while True:
    number = input("Enter a number: ")
    if number == "stop":
        break
    numbers.append(int(number))


average = sum(numbers)/ len(numbers)
print("average: ", average)






