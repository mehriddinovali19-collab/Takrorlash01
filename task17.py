students = {"Ali":90, "Vali":85, "Soli":95}
best_student = max(students, key=students.get)
grade = students[best_student]
print(best_student, grade)


