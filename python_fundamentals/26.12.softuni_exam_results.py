stats_dictionary = {}
submissions_counter = {} # counter increases with each submission, no matter if it's from the same student

while True:
    info = input()

    if info == "exam finished":
        print("Results:")
        for students_and_grades in stats_dictionary.values():
            for student, grade in students_and_grades.items():
                print(f"{student} | {grade}")
        print("Submissions:")
        for language, stats in submissions_counter.items():
            print(f"{language} - {stats}")
        break


    info_list = info.split("-")
    username = info_list[0]

    banned_user = False
    double_submission_same_language = False

    if "banned" == info_list[1]:
        banned_user = True


    if not banned_user:
        language = info_list[1]
        points = int(info_list[2])

        if language not in stats_dictionary.keys():
            # stats_dictionary[language] = {"username" : "", "points" : 0}
            stats_dictionary[language] = {}

        if language not in submissions_counter.keys():
            submissions_counter[language] = 0

        for exam_lang, user_stats_dictionary in stats_dictionary.items():
            if exam_lang == language:
                for student_name, current_points in user_stats_dictionary.items():
                    if username == student_name:
                        double_submission_same_language = True
                        submissions_counter[language] += 1
                        if current_points < points:
                            stats_dictionary[language][username] = points

        if not double_submission_same_language:
            stats_dictionary[language][username] = points
            submissions_counter[language] += 1
    else:
        for lang_, student_info in stats_dictionary.items():
            for name, grade in student_info.items():
                if username == name:
                    stats_dictionary[lang_].pop(username)
                    break


