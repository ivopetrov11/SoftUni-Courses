times = int(input())
word = input()
sentences_list = []
filtered_list = []

for i in range(times):
    sentence = input()
    sentences_list.append(sentence)

print(sentences_list)

for j in range(len(sentences_list)):
    if word in sentences_list[j]:
        #print(sentences_list[j])
        filtered_list.append(sentences_list[j])

print(filtered_list)
