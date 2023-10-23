#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Safely print the first x elements of a list
    Args:
        my_list (list): The list containing elements to be printed.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements printed
    """    
    try:
        for index in range(x):
            print(my_list[index], end=' ')
    except IndexError:
        pass

    print()
    return min(x, len(my_list))
