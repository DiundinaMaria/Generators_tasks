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
    """Выживает клетка с единственным соседом"""
    return '1' if curr_cell == '1' and (prev_cell == '1' or next_cell == '1') and not (
            prev_cell == '1' and next_cell == '1') else '0'


def born_or_not(prev_cell: str, curr_cell: str, next_cell: str) -> str:
    """Клетка рождается, если у неё 1 или 2 живых соседа"""
    return '1' if prev_cell == '1' or curr_cell == '1' or next_cell == '1' else '0'


data = convert('04052001')
res = []
for i in range(100):
    survived_cells = survive_or_not('0', data[0], data[1])
    for j in range(1, 31):
        survived_cells += survive_or_not(data[j - 1], data[j], data[j + 1])
    survived_cells += survive_or_not(data[30], data[31], '0')
    born_cells = born_or_not('0', survived_cells[0], survived_cells[1])
    for j in range(1, 31):
        born_cells += born_or_not(survived_cells[j-1], survived_cells[j], survived_cells[j+1])
    born_cells += born_or_not(survived_cells[30], survived_cells[31], '0')
    res.append(born_cells)
    data = born_cells

with open('result_1.txt', mode='w') as result:
    result.write('\n'.join(res))
