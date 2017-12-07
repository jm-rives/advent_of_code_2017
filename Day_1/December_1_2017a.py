from challenge import *
from Tests_December_1_2017a import *

def inverse_captcha(input):
    """ This function takes of string of numbers. The function returns the sum of the matching indices and assumes the list is circular."""
    index_in_input = 0
    next_index_in_input = index_in_input + 1
    sum_of_matched = 0
    last_index_in_input = input[-1]

    for item in range(0,len(input)-1):

        if input[index_in_input] == input[next_index_in_input]:
            sum_of_matched = int(input[index_in_input]) + sum_of_matched
            index_in_input += 1

            if (next_index_in_input + 1) != last_index_in_input:
                next_index_in_input += 1

        else:
            # print("ELSE block ran")
            index_in_input += 1
            next_index_in_input += 1

    if  input[0] == last_index_in_input:
        sum_of_matched = sum_of_matched + int(last_index_in_input)

    return sum_of_matched

challenge = list(str(challenge))
print(inverse_captcha(challenge))
