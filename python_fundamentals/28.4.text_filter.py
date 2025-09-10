banned_words_list = input().split(", ")
text = input()

for each_word in banned_words_list:
    text = text.replace(each_word, "*"*len(each_word))

print(text)