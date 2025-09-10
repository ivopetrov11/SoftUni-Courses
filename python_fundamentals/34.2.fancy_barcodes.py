import re

number_of_inputs = int(input())

for _ in range(number_of_inputs):
    valid_barcode = False
    has_numbers = False
    product_group = ""
    barcode = input()

    pattern = r"((@[#]+)([A-Z]{1})([A-Za-z\d]{4,})([A-Z]{1})(@[#]+))"
    num_pattern = r"([\d]+)"

    validity_check = re.match(pattern, barcode)

    if validity_check:
        # print(f"Valid - {barcode}")
        valid_barcode = True
        # print(validity_check.group(1))
    else:
        print("Invalid barcode")

    if valid_barcode:
        product_group = re.findall(num_pattern,barcode)
        if not product_group:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(product_group)}")