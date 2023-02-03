def list_summ_max(*args):
    the_sum = 0
    maximum = args[0]
    for i in args:
        the_sum = the_sum + i
        if i > maximum:
            maximum = i
    print(the_sum, maximum)

list_summ_max(1, 3, 54, 3)