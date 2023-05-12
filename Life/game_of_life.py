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


def survive_or_not(prev_cell: str, curr_cell: str, next_cell: str) -> str:
    return '1' if (
                          curr_cell == '1' and (prev_cell == '1' or next_cell == '1')) or (
                          curr_cell == '0' and (
                          (prev_cell == '1' or next_cell == '1') or (prev_cell == '1' and next_cell == '1'))) \
        else '0'


data = convert('04052001')
res = []
for i in range(100):
    next_iter_cells = survive_or_not('0', data[0], data[1])
    for j in range(1, 31):
        next_iter_cells += survive_or_not(data[j - 1], data[j], data[j + 1])
    next_iter_cells += survive_or_not(data[30], data[31], '0')
    res.append(next_iter_cells)
    data = next_iter_cells
print('\n'.join(res))
