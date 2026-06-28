age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 25:
    print("Young adult")
else:
    print("Adult")
