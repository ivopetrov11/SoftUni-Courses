deck = input() #original sequence of cards
shuffle_count = int(input()) #number of shuffles

current_shuffle = deck.split(" ") #splitting by space the deck string into a list
new_shuffle = []

#list splitting function
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]     # example usage -> B, C = split_list(A)

# current_left_deck, current_right_deck = split_list(current_shuffle)
new_left, new_right = split_list(current_shuffle)

for shuffle in range(1, shuffle_count + 1):

    for card in range(len(current_shuffle)//2):
        new_shuffle.append(new_left[card])
        new_shuffle.append(new_right[card])

    new_left, new_right = split_list(new_shuffle)

    current_shuffle = new_shuffle # new_shuffle becomes current_shuffle
    new_shuffle = []

print(current_shuffle)