#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Safely print the first x elements of a list
    Args:
        my_list (list): The list containing elements to be printed.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements printed
    """
    ret = 0
    for i in range(x):
        try:
            print(my_list[i], end=' ')
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
