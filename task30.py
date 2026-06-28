# Foydalanuvchidan uchta sonni kiritishni so'raymiz
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
c = float(input("Uchinchi sonni kiriting: "))

if a >= b and a>= c:
    eng_katta = a
elif b>= a and b>= c:
    eng_katta = b
else:
    eng_katta = c

print(f"Eng katta son: {eng_katta}")
