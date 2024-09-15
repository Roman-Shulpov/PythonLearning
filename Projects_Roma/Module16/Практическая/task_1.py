one = [1, 5, 3]
two = [1, 5, 1, 5]
three = [1, 3, 1, 5, 3, 3]

one.extend(two)
number_of_digits_five = one.count(5)
print(number_of_digits_five)
for _ in range(number_of_digits_five):
    one.remove(5)

one.extend(three)
number_of_digits_three = one.count(3)
print(number_of_digits_three)
print(one)
