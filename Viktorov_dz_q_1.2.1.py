# for num in range (1, 1001, 2):
#     cub_numb = num ** 3
#     sum_cub = 0
#     while cub_numb > 0:
#         digit = cub_numb % 10
#         sum_cub = sum_cub + digit
#         cub_numb = cub_numb // 10
#         print(sum_cub)
array = []
x = 0
for x in range(len(array)):
    y = int(array[x]) // 100000000 + int(array[x]) // 10000000 % 10 + int(array[x]) // 1000000 % 10 + int(
        array[x]) // 100000 % 10 + int(array[x]) // 10000 % 10 + int(array[x]) // 1000 % 10 + int(
        array[x]) // 100 % 10 + int(array[x]) // 10 % 10 + int(array[x]) % 10
    array[x] = array[x] + 17
x = 0
sum_17 = 0
while x < len(array):
    if array[x] % 7 == 0:
        sum_17 = sum_17 + array[x]
        x += 1
    else:
        x += 1
print("Сумма значений массива + 17, которые делятся на '7' без остатка:", sum_17)