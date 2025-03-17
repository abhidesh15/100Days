# numbers = [1, 3, 10, 974, 729, 281, 9272, 7593, 92738271, -1]
# #
# # max_num = 0
# #
# # for num in numbers:
# #     if num > max_num:
# #         max_num = num
#
# # print("Max num is: ", max_num)
# print("Max num is: ", max(numbers))

numbers = range(1, 101)

total = 0

# print("Total of numbers between 1 and 100 is:", sum(numbers))
for num in numbers:
    total += num

print(total)
