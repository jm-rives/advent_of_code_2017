from file_reader import *

results = []

for row in rows:

    big_num = None
    little_num = None

    for elem in row:
        # print(f"Current Elem is: {elem}")

        if big_num == None and little_num == None:
            big_num = int(elem)
            little_num = int(elem)
            # print(f"Little Num p 'if' is now: {little_num}")
            # print(f"\nBig Num p 'if' is now: {big_num}\n")

        elif int(elem) > big_num:
            big_num = int(elem)
            # print(f"Little Num p '1st elif' is now: {little_num}\n")
        elif int(elem) < little_num:
            little_num = int(elem)
            # print(f"Little Num p '2nd elif' is now: {little_num}\n")
        else:
            pass


    # print(f"\nBig Num is now: {big_num}")
    # print(f"Little Num is now: {little_num}\n")
    result = int(big_num) - int(little_num)
    # print(f"Result is: {result}\n")
    results.append(result)

checksum = 0
for result in results:
    checksum += result
print(checksum)
