#!/usr/bin/python3
"""
defines function to find peak in list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted ints
    """
    if list_of_integers is None or list_of_integers == []:
        return None
    mid = int(len(list_of_integers) / 2)
    if len(list_of_integers) % 2 == 0:
        mid = mid - 1
    middle = list_of_integers[mid]
    low = list_of_integers[0]
    high = list_of_integers[-1]
    if middle is low and middle is high:
        return middle
    if middle is low and middle > list_of_integers[mid + 1]:
        return middle
    if middle > list_of_integers[mid + 1]:
        if middle > list_of_integers[mid - 1]:
            return middle
        else:
            peak_low = find_peak(list_of_integers[:mid])
            if peak_low is not None:
                return peak_low
    else:
        peak_high = find_peak(list_of_integers[(mid + 1):])
        if peak_high is not None:
            return peak_high
