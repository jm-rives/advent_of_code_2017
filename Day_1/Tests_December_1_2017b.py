from December_1_2017b import *
################
#### TESTS #####
################

input1 = '1212'
input2 = '1221'
input3 = '123425'
input4 = '123123'
input5 = '12131415'

print(inverse_captcha_halfway_around(challenge))


if inverse_captcha_halfway_around(input1) != 6:
    print("FAIL")
else:
    print(f"{inverse_captcha_halfway_around(input1)} * PASS * PASS * PASS * PASS *")

if inverse_captcha_halfway_around(input2) != 0:
    print("FAIL")
else:
    print(f"{inverse_captcha_halfway_around(input2)} * PASS * PASS * PASS * PASS *")

if inverse_captcha_halfway_around(input3) != 4:
    print(f"{inverse_captcha_halfway_around(input3)} --> FAIL")
else:
    print(f"{inverse_captcha_halfway_around(input3)} * PASS * PASS * PASS * PASS *")

if inverse_captcha_halfway_around(input4) != 12:
    print(f"{inverse_captcha_halfway_around(input4)} --> FAIL")
else:
    print(f"{inverse_captcha_halfway_around(input4)} * PASS * PASS * PASS * PASS *")

if inverse_captcha_halfway_around(input5) != 4:
    print(f"{inverse_captcha_halfway_around(input5)} -FAIL")
else:
    print(f"{inverse_captcha_halfway_around(input5)} * PASS * PASS * PASS * PASS *")
