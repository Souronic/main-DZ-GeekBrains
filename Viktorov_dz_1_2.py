odd_numb = 1
cub_numb = ""
sum_cub = ""
while odd_numb < 1000:
    odd_numb += 1
    if odd_numb % 2 != 0:
        cub_numb = odd_numb ** 3
        sum_cub = cub_numb // 100000000 + cub_numb // 10000000 % 10 + cub_numb // 1000000 % 10 + cub_numb // 100000 % 10 + cub_numb // 10000 % 10 + cub_numb // 1000 % 10 + cub_numb // 100 % 10 + cub_numb // 10 % 10 + cub_numb % 10
        if sum_cub % 7 == 0:
            print(odd_numb, "^3: ", cub_numb, "sum: ", sum_cub)
        else:
            pass
    else:
        pass



