# Python Mashqlari — 60 ta amaliy masala

Quyida siz bergan mavzular bo'yicha jami **60 ta masala** tayyorlandi. Har bir mavzu uchun 2-3 ta masala bor. Tartib bo'yicha yechib chiqing — har bir keyingi mavzu avvalgisiga asoslangan.

---

## 1. Numbers
1. Ikki sonni kiritib, ularning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini hisoblang.
2. Berilgan sonning tub son (prime) ekanligini tekshiruvchi dastur yozing.

## 2. List
3. Berilgan ro'yxatdagi eng katta va eng kichik elementni toping (`max()`/`min()` funksiyasidan foydalanmasdan).
4. Ro'yxatdagi takrorlanuvchi elementlarni olib tashlang.
5. Ro'yxatni teskari tartibda chiqaring (`reverse()` yoki slicing'dan foydalanmasdan, faqat `for` loop bilan).

## 3. Nested List
6. 3x3 matritsani nested list ko'rinishida yarating va uning diagonal elementlari yig'indisini toping.
7. Ikki nested listni (matritsalarni) element bo'yicha qo'shing.

## 4. List Slicing
8. Berilgan ro'yxatdan faqat juft index'dagi elementlarni slicing yordamida ajratib oling.
9. Ro'yxatni teng ikkiga bo'lib, ikkinchi yarmini birinchisidan oldin chiqaring (slicing yordamida).

## 5. List Comprehension
10. 1 dan 50 gachagi sonlardan faqat 3 ga bo'linadiganlarini list comprehension yordamida yig'ing.
11. Berilgan so'zlar ro'yxatidan faqat unli harf bilan boshlanadiganlarini ajratib oling.
12. Ikki o'lchamli (nested) list comprehension yordamida 5x5 ko'paytirish jadvalini hosil qiling.

## 6. Tuple
13. Tuple ichidagi elementlarning chastotasini (necha marta takrorlangani) hisoblang.
14. Ikkita tuple'ni birlashtirib, natijani saralangan (sorted) tuple sifatida qaytaring.

## 7. Set
15. Ikki ro'yxatdagi umumiy (kesishgan) elementlarni set yordamida toping.
16. Berilgan matndagi unique (takrorlanmaydigan) so'zlar sonini set yordamida hisoblang.

## 8. Dictionary
17. Talabalar ismi va bahosi saqlangan dictionary yarating, eng yuqori bahoga ega talabani toping.
18. Berilgan matndagi har bir harfning necha marta takrorlanganini dictionary'da saqlang.
19. Ikki dictionary'ni birlashtiring, agar kalit takrorlansa qiymatlarini qo'shib chiqaring.

## 9. Nested Dictionary
20. Har bir talabaning fanlar bo'yicha bahosini saqlaydigan nested dictionary yarating va o'rtacha bahoni hisoblang.
21. Nested dictionary ichida ma'lum bir kalitni qidirib, uning qiymatini yangilang.

## 10. Dict Comprehension
22. Berilgan ro'yxatdagi sonlarning kvadratini kalit-qiymat juftligida saqlovchi dict comprehension yozing.
23. Berilgan dictionary'dan faqat qiymati 50 dan katta bo'lgan juftliklarni ajratib oling.

## 11. String
24. Berilgan satrning palindrom (orqa-oldin bir xil o'qiladigan) ekanligini tekshiring.
25. Matndagi har bir so'zning birinchi harfini katta qilib chiqaring (title case'ni qo'lda yozing).
26. Berilgan satrdagi unlilar sonini hisoblang.

## 12. String Slicing
27. Berilgan satrni teskari tartibda chiqaring (slicing yordamida, `[::-1]`).
28. Satrning faqat har 2-harfini slicing yordamida ajratib oling.

## 13. If...Elif...Else
29. Foydalanuvchi kiritgan yoshga qarab "bola", "o'smir", "kattalar" yoki "keksa" toifasini aniqlang.
30. Uchta sonni solishtirib, eng kattasini if-elif-else yordamida toping.

## 14. While Loop
31. `while` loop yordamida 1 dan 100 gachagi sonlar yig'indisini hisoblang.
32. Foydalanuvchidan son kiritishni "stop" so'zi kiritilguncha davom ettiring va kiritilgan sonlar o'rtachasini chiqaring.

## 15. For Loop
33. 1 dan 10 gacha sonlarning faktorialini chiqaring.
34. Fibonachchi ketma-ketligining birinchi 15 ta sonini chiqaring.
35. Berilgan ro'yxatdagi har bir elementni o'z indexi bilan birga chiqaring (`enumerate` yordamida).

## 16. Break Statement
36. 1 dan 100 gacha sonlarni tekshirib, birinchi 7 ga bo'linadigan sonni topib `break` bilan to'xtatib chiqaring.
37. Ro'yxat ichida berilgan elementni qidiring, topilgach loop'ni `break` bilan to'xtating.

## 17. Continue Statement
38. 1 dan 20 gacha sonlardan faqat toqlarini `continue` yordamida o'tkazib yuborib, juftlarini chiqaring.
39. Ro'yxatdagi manfiy sonlarni `continue` bilan o'tkazib, faqat musbat sonlarning yig'indisini hisoblang.

## 18. Functions
40. Berilgan sonning faktorialini hisoblovchi funksiya yozing.
41. Ikki son orasidagi barcha tub sonlarni qaytaruvchi funksiya yozing.
42. Default va keyword argumentlardan foydalanib, talaba ma'lumotlarini chiqaruvchi funksiya yarating.

## 19. Lambda Function
43. Lambda funksiya yordamida ikkita sonning ko'paytmasini hisoblang.
44. Ro'yxatdagi sonlarni lambda funksiya yordamida kamayish tartibida saralang (`sorted()` + `key`).

## 20. Variables Scope
45. Global va local o'zgaruvchilar orasidagi farqni ko'rsatuvchi dastur yozing (`global` kalit so'zidan foydalaning).
46. Funksiya ichida `nonlocal` kalit so'zidan foydalanib, ichki funksiyada tashqi funksiya o'zgaruvchisini o'zgartiring.

## 21. Classes and Objects
47. `Car` klassini yarating: marka, model, narx atributlari va ma'lumotni chiqaruvchi metod bilan.
48. `BankAccount` klassi yarating: pul qo'yish (`deposit`), yechish (`withdraw`) va balansni ko'rsatish metodlari bilan.
49. `Book` klassidan bir necha obyekt yaratib, ularni ro'yxatda saqlang va narxi bo'yicha saralang.

## 22. Inheritance
50. `Animal` klassidan `Dog` va `Cat` klasslarini meros qilib oling, har biri uchun `sound()` metodini qayta yozing (override).
51. `Person` klassidan `Student` klassini meros qilib oling, qo'shimcha "fakultet" atributi bilan.
52. `Shape` klassidan `Circle` va `Rectangle` klasslarini hosil qiling, har biri o'z yuzasini hisoblaydigan metodga ega bo'lsin.

## 23. Read/Write Txt Files
53. Foydalanuvchidan kiritilgan matnni `notes.txt` fayliga yozib saqlang.
54. `notes.txt` faylini o'qib, undagi qatorlar sonini va so'zlar sonini hisoblang.

## 24. Read/Write CSV Files
55. Talabalar ismi va bahosini o'z ichiga olgan ma'lumotlarni `students.csv` fayliga yozing.
56. `students.csv` faylini o'qib, eng yuqori bahoga ega talabani aniqlang.
57. CSV fayldagi ma'lumotlarni dictionary ko'rinishida (`DictReader`) o'qib, ekranga chiqaring.

## 25. Exception Handling
58. Foydalanuvchidan son kiritishni so'rang va agar son emas narsa kiritilsa, `try-except` yordamida xatolikni ushlang.
59. Nolga bo'lish (`ZeroDivisionError`) xatoligini `try-except-finally` bilan boshqaring.
60. Maxsus (custom) exception klass yaratib, berilgan yosh manfiy bo'lsa shu xatolikni chaqiring (`raise`).

---

**Maslahat:** Har bir masalani yechishdan oldin, avval qog'ozda yoki izoh sifatida algoritmni qisqacha yozib oling, keyin kodga o'tkazing. Agar biror masalada qiynalsangiz, ayting — birga ko'rib chiqamiz.
