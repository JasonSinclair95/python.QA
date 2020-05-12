def even_nums(item1, item2):
    for numbers in range(item1, item2):
        if numbers % 2 == 0:
            print(numbers, end=', ')

range_1=int(input('please enter beginning of range: '))
range_2=int(input('please enter end of range: '))

even_nums(range_1, range_2)