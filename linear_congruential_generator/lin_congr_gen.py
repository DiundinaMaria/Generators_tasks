NUM_IN_GROUP = 4

with open('prime_numbers.txt') as file:
    str_nums = file.read().split()
    prime_nums = []
    for str_num in str_nums:
        prime_nums.append(int(str_num))


def get_prime(index) -> int:
    return prime_nums[index - 1]


x = NUM_IN_GROUP
a = get_prime(NUM_IN_GROUP + 3)
b = get_prime(NUM_IN_GROUP + 7)
p = get_prime(4 * NUM_IN_GROUP + 1)

res = []
for i in range(100):
    x = (a * x + b) % p
    res.append(str(x))

with open('result_prime.txt', mode='w') as result:
    result.write('\n'.join(res))
