
########## The Specs ##########
# 1) Timebox: 1 millisecond
# 2) accept a sequence of digits
# ------ copy paste it vs read file
# 3) find the sum of all digits that match the next digits in the list
# ------ sounds like a job for a loop
# ------ list comphrehension
# ------- read the initital index
# if first and last digit match add the last digit to the sum ( circular list)

input = 1122

input = list(str(input))
# print(range(len(input)))

def inverse_captcha(input):
    """ This function takes of string of numbers. The function returns the sum of the matching indices in assuming the list is circular."""
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

            # print(f"CURRENT INDEX {index_in_input}")
            # print(f"NEXT INDEX {next_index_in_input}")
            # print(f"Some of matched is: {sum_of_matched}")
            # print(f"Next next loop = {index_in_input} \n")

        else:
            # print("ELSE block ran")
            index_in_input += 1
            next_index_in_input += 1
            # print(f"CURRENT INDEX {index_in_input}")
            # print(f"NEXT INDEX {next_index_in_input}")
            # print(f"Some of matched is: {sum_of_matched}")



    if  input[0] == last_index_in_input:
        sum_of_matched = sum_of_matched + int(last_index_in_input)

    return sum_of_matched


###### Tests ########
if inverse_captcha(input) != 3:
    print("FAIL")
else:
    print(f"{inverse_captcha(input)}* PASS * PASS * PASS * PASS *")

more_input = '1111'
if inverse_captcha(more_input) != 4:
    print("FAIL")
else:
    print(f"{inverse_captcha(more_input)}* PASS * PASS * PASS * PASS *")

way_more_input = "1234"
if inverse_captcha(way_more_input) != 0:
    print(f"{inverse_captcha(last_test_input)} --> FAIL")
else:
    print(f"{inverse_captcha(more_input)}* PASS * PASS * PASS * PASS *")

last_test_input = "91212129"
if inverse_captcha(last_test_input) != 9:
    print(f"{inverse_captcha(last_test_input)} -FAIL")
else:
    print(f"{inverse_captcha(last_test_input)}* PASS * PASS * PASS * PASS *")
