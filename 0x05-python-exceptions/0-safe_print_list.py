#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for index in range(x):
            print(my_list[index], end=' '):
    except IndexError:
        pass

    print()
    return min(x, len(my_list))