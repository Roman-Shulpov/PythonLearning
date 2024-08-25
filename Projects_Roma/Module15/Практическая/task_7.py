word = input("Введите слово: ")
list_word = list(word)
index = len(list_word)

a = 0
count = 0
for i in range(index//2):
    if list_word[i] == list_word[index-1-a]:
        count += 1
    a += 1
if count == index//2:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
