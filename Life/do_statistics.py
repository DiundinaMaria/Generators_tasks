from scipy.stats import kstest, chisquare

FILE_NAME = 'result_2.txt'

with open(FILE_NAME) as file:
    lines = [int(line, 2) for line in file.readlines()]
    function_sequence = []
    for i in range(1, 101):
        function_sequence.append(i * i)
    print(f"Тест Колмогорова-Смирнова {kstest(lines, function_sequence)}")
    print(f"Тест хи-квадрат: {chisquare(lines, function_sequence)}")
