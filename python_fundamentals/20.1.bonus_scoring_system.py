import math

students = int(input())
lectures = int(input())
bonus= int(input())

# SOLUTION FROM THE LECTURER
# dynamic variables in which only the latest calculated value will be stored if higher than the previous one
max_bonus = 0
max_bonus_attendances = 0

if lectures:
    for student in range(students):
        attendance = int(input())
        total_bonus = attendance / lectures * (5 + bonus)

        if total_bonus > max_bonus:
            # max_bonus becomes the latest calculated total_bonus if total_bonus is higher than the value of max_bonus
            max_bonus = total_bonus
            # attendance is analogically assigned to the max_bonus_attendances variable
            max_bonus_attendances = attendance

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_bonus_attendances} lectures.")

# THIS GIVES 90/100 IN JUDGE - CAN'T FIND THE REASON FOR NOW
# if students not in range (0, 51) or lectures not in range (0, 51) or bonus not in range (0, 101):
#     exit()
#
# attendance_list = []
#
# for student in range(1, students + 1):
#     attendance = int(input())
#     if attendance > lectures:
#         attendance = lectures
#
#     attendance_list.append(attendance)
#
# def total_bonus(n: int):
#     return n / lectures * (5 + bonus)
#
# bonus_list = list(map(total_bonus, attendance_list))
# # print(bonus_list)
#
# if bonus_list:
#     max_bonus = max(bonus_list)
#     attended_lectures = attendance_list[bonus_list.index(max_bonus)]
#
#     print(f"Max Bonus: {math.ceil(max_bonus)}.")
#     print(f"The student has attended {attended_lectures} lectures.")