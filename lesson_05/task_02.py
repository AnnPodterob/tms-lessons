def list_num(num_list: list) -> int:
    the_sum = 0
    for i in num_list:
        the_sum += i
    return the_sum

print(list_num([1,31,32,2,4]))
print(list_num([54,32,53,3]))
