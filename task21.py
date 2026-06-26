def update_grade(data):
    name_student = input("Name of the stduent: ")
    name_subject = input("Name of the subject: ")
    new_grade = int(input("What's grade: "))

    for name_student in data:
        if name_student in data[name_student]:
            data[name_student][name_subject] = new_grade
            print("New grade passed seccussfully!")
        else:
            print("Subject not founded")
    else:
        print("Student not founded ")



data = {
    "Ali": {"mat": 90, "fizika": 80},
    "Vali": {"mat": 85, "fizika": 75}
}

print(update_grade(data))

