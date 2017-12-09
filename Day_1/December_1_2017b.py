from challenge import *

def inverse_captcha_halfway_around(stuff):
    """This function compares two
       equidistant numbers in a list and
       sums the matched numbers. """

    stuff = list(stuff)

    half = len(stuff) / 2
    #half = int(half)

    list_a = stuff[0:half]
    list_b = stuff[half: ]

    #index = 0

    sum_of_matched = 0

    for index in range(len(list_a)):
        if list_a[index] == list_b[index]:
            sum_of_matched += int(list_a[index])

    return sum_of_matched * 2
