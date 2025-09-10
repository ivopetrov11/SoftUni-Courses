countries_list = input().split(", ")
capitals_list = input().split(", ")
output_dictionary = dict(zip(countries_list,capitals_list))

for key, value in output_dictionary.items():
    print(f"{key} -> {value}")