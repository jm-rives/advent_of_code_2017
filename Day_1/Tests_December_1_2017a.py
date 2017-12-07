from December_1_2017a.py import *
# challenge
print(inverse_captcha(challenge)

##### Tests ######
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
