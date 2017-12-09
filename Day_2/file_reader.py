path = '/Users/joannarives/advent_of_code_2017/Day_2/input.txt'

input_file = open(path, 'r')

# def file_contents(input_file):
rows = []
for line in input_file:
    row = line.split('\t')
    new_last = row[-1].strip('\n')
    row = row[:-1]
    row.append(new_last)
    # row[-1].strip('\n')
    rows.append(row)

    # return rows
