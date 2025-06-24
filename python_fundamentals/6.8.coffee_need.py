# The list of events can contain the following:
# · You have homework to do ("coding").
# · You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
# · You watch a movie ("movie").
# · If other events are present, they will be represented by arbitrary strings. Just ignore them!

#from curses.ascii import isupper

# def check_upper(letter):
#     if ord(letter) < 96:
#         return True
#     else:
#         return False

command = input()
coffee_amount = 0

while command != "END":

    if command.lower() in ("coding", "dog", "cat", "movie"):
        if command.isupper():
            coffee_amount += 2
        else:
            coffee_amount += 1
    # else:
    #     continue

    command = input()

else:
    if coffee_amount <= 5:
        print(coffee_amount)
    else:
        print("You need extra sleep")