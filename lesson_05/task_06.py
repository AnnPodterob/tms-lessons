def filter_odd_number(int_num: list) -> list:
    new_list = [i for i in int_num if i % 2 == 0]
    print(new_list)

filter_odd_number([1,3,2,4,7,4])