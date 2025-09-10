first_string, second_string = input().split()
total_sum = 0

def bigger_str(smaller_str: str, larger_str: str):
    total_char_sum = 0
    for index in range(len(smaller_str)):
        total_char_sum += ord(smaller_str[index]) * ord(larger_str[index])
    for remainder in range(len(smaller_str), len(larger_str)):
        total_char_sum += ord(larger_str[remainder])
    print(total_char_sum)

if len(first_string) < len(second_string):
  bigger_str(first_string,second_string)
elif len(first_string) > len(second_string):
  bigger_str(second_string, first_string)
else:
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    print(total_sum)