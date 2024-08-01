#!/usr/bin/python3
'''This module contains a function that checks
if all the boxes can be opened'''


def open_box(boxes, number, numbers_list):
    '''This function opens the boxes and checks
    if all the boxes can be opened'''
    numbers_list.add(number)
    for c_number in boxes[number]:
        is_valid = c_number >= 0 and c_number < len(boxes)
        is_new = c_number not in numbers_list
        if isinstance(c_number, int) and is_valid and is_new:
            open_box(boxes, c_number, numbers_list)


def canUnlockAll(boxes):
    '''This function checks if all the boxes can be opened'''
    numbers_list = set()
    current_numbers = set([0])
    while len(current_numbers) > 0:
        new_numbers = set()
        for current_number in current_numbers:
            numbers_list.add(current_number)
            for number in boxes[current_number]:
                is_valid = number >= 0 and number < len(boxes)
                is_new = number not in numbers_list
                if isinstance(number, int) and is_valid and is_new:
                    new_numbers.add(number)
        current_numbers = new_numbers
    return len(numbers_list) == len(boxes)
