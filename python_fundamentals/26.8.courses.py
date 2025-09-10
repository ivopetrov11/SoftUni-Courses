courses_dictionary = {}

while True:
    info = input()

    if info == "end":
        for course, students in courses_dictionary.items():
            print(f"{course}: {len(students)}")
            for each_student in students:
                print(f"-- {each_student}")
        break

    info_list = info.split(" : ")
    course_name = info_list[0]
    student_name = info_list[1]

    if course_name not in courses_dictionary.keys():
        courses_dictionary[course_name] = []
    courses_dictionary[course_name].append(student_name)