#!/usr/bin/python3
"""Defines a function that divides two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists element by element.

    Args:
        my_list_1 (list): The list of numerators.
        my_list_2 (list): The list of denominators.
        list_length (int): The length of the resulting list.

    Returns:
        list: A new list containing the results of each division,
              with 0 in place of any division that couldn't be done.
    """
    new_list = []

    for i in range(list_length):
        try:
            division_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except TypeError:
            print("wrong type")
            division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            new_list.append(division_result)

    return new_list
