def palindrom(text: str):
    if text.lower() == text[::-1].lower():
        return f"This is palindrom: {text}"
    else:
        return f"This is not palindrom, please enter another word! {text}"


text = input("Enter a word: ")
print(palindrom(text))
