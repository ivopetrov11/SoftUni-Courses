import math

budget = float(input())
students = int(input())
flour_price = float(input())
eggs_price = float(input()) * 10
apron_price = float(input())

flour_pcs = 0
eggs_pcs = 0
aprons = 0

for student in range(1, students + 1):
    if student % 5 == 0:
        flour_pcs += 0
    else:
        flour_pcs += 1
    eggs_pcs += 1
    aprons += 1

total_flour = f"{flour_pcs * flour_price:.2f}"
total_eggs = f"{eggs_pcs * eggs_price:.2f}"
aprons *= 1.2
# aprons = math.ceil(aprons)
total_aprons = f"{math.ceil(aprons) * apron_price:.2f}"

totals =  float(total_flour) + float(total_eggs) + float(total_aprons)
# print(total_flour)
# print(total_eggs)
# print(total_aprons)
# print(totals)

if float(totals) <= budget:
    print(f"Items purchased for {totals:.2f}$.")
else:
    print(f"{float(totals) - budget:.2f}$ more needed.")
