word_count = int(input())
synonym_dictionary = {}
word_list = []

for _ in range(word_count * 2):
    word_input = input()
    word_list.append(word_input)

for index in range(0, len(word_list),2):
    word = word_list[index]
    # print(index)
    synonym = word_list[index + 1]
    # print(index + 1)
    if word not in synonym_dictionary.keys():
        synonym_dictionary[word] = []
    synonym_dictionary[word].append(synonym)

for key, value in synonym_dictionary.items():
    print(f"{key} - {', '.join(value)}")