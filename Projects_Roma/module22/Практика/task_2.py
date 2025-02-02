# with open('txt.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)
#
summ = 0

def get_content(filename):
    with open(filename, 'r') as file:
        return file.read()


content = get_content('txt.txt')
content = content.replace(' ', '')
numbers = content.split('\n')
for num in numbers:
    int_num = int(num)
    summ = summ + int_num

print(numbers)
print(summ)
