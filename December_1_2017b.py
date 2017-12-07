def inverse_captcha_halfway_around(stuff):
    """This function compares two
       equidistant numbers in a list and increments
       sums the matched numbers. """

    stuff = list(stuff)
    # print(stuff)
    half = len(stuff) / 2
    # print(half)
    half = int(half)

    list_a = stuff[0:half]
    list_b = stuff[half: ]
    # print(list_b[-1])
    # print(f"List A is: {list_a}")
    # print(f"List B is: {list_b}")
    index = 0
    sum_of_matched = 0
    for item in list_a:

        if list_a[index] == list_b[index]:
            sum_of_matched = int(list_a[index]) + sum_of_matched
            index += 1
        else:
            index += 1

    return sum_of_matched
################
#### TESTS #####
################
input1 = '1212'
input2 = '1221'
input3 = '12345'
input4 = '123123'
input5 = '12131415'

print(inverse_captcha_halfway_around(input1))
# if inverse_captcha_halfway_around((input1) != 6:
#     print("FAIL")
#
# else:
#     print(f"{inverse_captcha_halfway_around((input)}* PASS * PASS * PASS * PASS *")

#
# if inverse_captcha_halfway_around((input2) != 0:
#     print("FAIL")
# else:
#     print(f"{inverse_captcha_halfway_around((more_input)}* PASS * PASS * PASS * PASS *")
#
#
# if inverse_captcha_halfway_around((input3) != 4:
#     print(f"{inverse_captcha_halfway_around((last_test_input)} --> FAIL")
# else:
#     print(f"{inverse_captcha_halfway_around((more_input)}* PASS * PASS * PASS * PASS *")
#
#
# if inverse_captcha_halfway_around((input4) != 12:
#     print(f"{inverse_captcha_halfway_around((last_test_input)} -FAIL")
# else:
#     print(f"{inverse_captcha_halfway_around((last_test_input)}* PASS * PASS * PASS * PASS *")
#
# if inverse_captcha_halfway_around((input5) != 4:
#     print(f"{inverse_captcha_halfway_around((last_test_input)} -FAIL")
# else:
#     print(f"{inverse_captcha_halfway_around((last_test_input)}* PASS * PASS * PASS * PASS *")
