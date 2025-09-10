students_courses = {}
# keys - courses, values - lists with names and IDs
search_course = ""

while True:
    command = input()
    if ":" not in command:
        search_course = command
        break

    data = command.split(":")
    key_course = data[2] # setting up the course i.e. the key
    # then will create an empty list as a value to this key and append the students in it
    if key_course not in students_courses.keys():
        students_courses[key_course] = []
    students_courses[key_course].append(data[0])
    students_courses[key_course].append(data[1])

for course in students_courses.keys():
    if course.startswith(search_course[0:5]):
        for index in range(0, len(students_courses[course]), 2):
            name = students_courses[course][index]
            id_ = students_courses[course][index + 1]
            print(f"{name} - {id_}" )
