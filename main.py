def even_number_filter(num_list: list):
    index = -1
    while index < len(num_list)-1:
        index += 1
        if num_list[index] % 2 == 0:
            yield num_list[index]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = even_number_filter(numbers)
for num in even_nums:
    print(num)
