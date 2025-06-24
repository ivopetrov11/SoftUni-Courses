names_list = input().split(", ") #list created from the direct input of names

sorted_list = sorted(names_list, key=lambda x:(-len(x),x))
# ANOTHER IMPORTANT LESSON -> sorted() works with how many arguments the function returns

#in the case above - the lambda func returns two arguments - the reverse length of the items in the list and the list itself
# lambda x: — For every item x (a name) in the list… [TAKES EACH ITEM FROM THE LIST]
# -len(x) — Step one of sorting: get the length of the name and flip it negative to make longer names come first (since sorting defaults to smallest-to-largest).
# x — Step two: if two names have the same length, compare them alphabetically.

print(sorted_list)