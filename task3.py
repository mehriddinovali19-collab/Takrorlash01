def max_num(numbers):
    return max(numbers)

def min_mun(numbers):
    return min(numbers)    

def main():
    option = input("Find max or min of number: ")
    number = [4, 9, 2, 7, 1]
    if option.lower() == "max".lower():
        max1 = max_num(number)
        print(f'Max of the number {max1}')
    elif option.lower() == "min".lower():
        min1 =min_mun(number)
        print(f'Min of the number {min1}')

main()
    