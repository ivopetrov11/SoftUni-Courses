pair_input_number = int(input())

students_dictionary = {}

for _ in range(pair_input_number):
    name = input()
    grade = float(input())

    if name not in students_dictionary.keys():
        students_dictionary[name] = []
    students_dictionary[name].append(grade)

for student, grades in students_dictionary.items():
    average = sum(grades) / len(grades)
    # if average < 4.5:
    #     students_dictionary.pop(student)
    # else:
    #     print(f"{student} -> {average:.2f}")
    if average >= 4.5:
        print(f"{student} -> {average:.2f}")