command_list = input().split()

for word in command_list:
    # creating empty strings within the loop to store separately the digits and the letters
    # with each iteration, the strings are reset, so the previous iteration would not interfere
    number_letter = ""
    letters = ""

    # checking if each char in the current word is a digit or a letter and adding it to the respective string
    for char in word:
        if char.isdigit():
            # N.B.! This checks if the char is a digit, but it DOES NOT transform it into a digit (int) - IT STAYS AS A STRING type
            # concatenating each digit char to the number_letter string
            number_letter += char
        else:
            letters += char

    # covering the case where the second and the last letter of each word are switched
    # this only happens when there are two or more letters in the letters-part of the word
    # therefore - if the check is valid,
    # we get the last letter by index [-1], add the letters in between the first and last index [1:-1] (it would return an empty string if the word is only 2 letters, which still is fine)
    # and then add the first letter by index [0]
    if len(letters) >= 2:
        letters = letters[-1] + letters[1:-1] + letters[0]

    deciphered = chr(int(number_letter)) + letters
    # each word-iteration is printed on the same row with space in the end, as the end=" " keeps the output in one line
    print(deciphered, end=" ")