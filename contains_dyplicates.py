def contains_dyplicates(example_list):
    #количество элементов не равно количеству элементов массива
    return len(set(example_list)) != len(example_list)

#example_list = [1, 2, 3, 4] => False
#example_list = [1, 2, 3, 1] => True
#example_list = [] => False
example_list = []
print(contains_dyplicates(example_list))