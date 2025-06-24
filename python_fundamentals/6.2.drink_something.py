# A kid is defined as someone under or at the age of 14.
# A teen is defined as someone under or at the age of 18.
# A young adult is defined as someone under or at the age of 21.
# An adult is defined as someone above the age of 21.
# Note: All the values are inclusive except the last one!

age = int(input())

if age <= 14:
    print("drink toddy")
elif 14 < age <= 18:
    print("drink coke")
elif 18 < age <= 21:
    print("drink beer")
elif 21 < age:
    print("drink whisky")