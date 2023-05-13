import textwrap


def convert(b_day: str) -> str:
    nums_str = textwrap.wrap(b_day, 2)
    nums = []
    for num in nums_str:
        num = int(num)
        nums.append(num)
    data = ''
    for num in nums:
        curr = ''
        while num > 0:
            curr += str(num % 2)
            num = num // 2
        curr = '0' * (8 - len(curr)) + curr[::-1]
        data += curr
    return data


def do_next_step(prev_cell: str, curr_cell: str, next_cell: str) -> str:
    if prev_cell == '1' and curr_cell == '1' and next_cell == '1':
        return '0'
    elif prev_cell == '1' and curr_cell == '1' and next_cell == '0':
        return '1'
    elif prev_cell == '1' and curr_cell == '0' and next_cell == '1':
        return '1'
    elif prev_cell == '1' and curr_cell == '0' and next_cell == '0':
        return '0'
    elif prev_cell == '0' and curr_cell == '1' and next_cell == '1':
        return '1'
    elif prev_cell == '0' and curr_cell == '1' and next_cell == '0':
        return '1'
    elif prev_cell == '0' and curr_cell == '0' and next_cell == '1':
        return '1'
    elif prev_cell == '0' and curr_cell == '0' and next_cell == '0':
        return '0'


data = convert('04052001')
res = []
for i in range(100):
    survived_cells = do_next_step('0', data[0], data[1])
    for j in range(1, 31):
        survived_cells += do_next_step(data[j - 1], data[j], data[j + 1])
    survived_cells += do_next_step(data[30], data[31], '0')
    res.append(survived_cells)
    data = survived_cells

with open('result_2.txt', mode='w') as result:
    result.write('\n'.join(res))
