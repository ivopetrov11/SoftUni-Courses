companies_dictionary = {}

while True:
    info = input()

    if info == "End":
        for company, employees in companies_dictionary.items():
            print(f"{company}")
            for each_employee in employees:
                print(f"-- {each_employee}")
        break

    info_list = info.split(" -> ")
    company_name = info_list[0]
    employee_id = info_list[1]

    if company_name not in companies_dictionary.keys():
        companies_dictionary[company_name] = []

    if employee_id in companies_dictionary[company_name]:
        continue
    else:
        companies_dictionary[company_name].append(employee_id)