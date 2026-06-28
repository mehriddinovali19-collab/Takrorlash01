def count_wovel(text: str):
    counted = 0

    for word in text:
        if word in "aoueiAUOEI":
            counted += 1
    return f"This is number of vowels in counted: {counted}"

text = "Python dasturlash"
print(count_wovel(text))