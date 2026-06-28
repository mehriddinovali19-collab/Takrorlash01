def backing_format(text: str):
    reverse = text[::-1]
    return reverse

text = input("Enter a text: ")
print(backing_format(text))