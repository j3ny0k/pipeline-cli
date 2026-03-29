def even(nums):
        return [x for x in nums if x % 2 == 0]
def odd(nums):
    return [x for x in nums if x % 2 != 0]
def double(nums):
    return [x * 2 for x in nums]
def square(nums):
    return [x ** 2 for x in nums]
def sort(nums):
    return sorted(nums)

ops = {
    'even': even,
    'odd': odd,
    'double': double,
    'square': square,
    'sort': sort
}

print('available operations:', ', '.join(ops))
print('type "help" to show operations again')
print('enter numbers separated by space (example: 1 2 3)')
print('enter operations separated by space (example: even double)\n')

while True:
    def parse_nums():
        while True:
            raw = input('nums: ').strip()

            if not raw:
                print('input is empty\n')
                continue

            try:
                return [int(x) for x in raw.split()]
            except ValueError:
                print('only integers allowed\n')

    nums = parse_nums()

    def parse_operations(ops):
        while True:
            raw = input('operations: ').strip()

            if not raw:
                print('input is empty\n')
                continue

            elif raw == 'help':
                print('available operations:', ', '.join(ops), '\n')
                continue

            operations = raw.split()

            invalid = [name for name in operations if name not in ops]

            if invalid:
                print('invalid operations:', ', '.join(invalid))
                print('available:', ', '.join(ops), '\n')
                continue

            return operations

    operations = parse_operations(ops)
    result = nums

    for name in operations:
        result = ops[name](result)

    def format_nums(nums):
        return [str(x) for x in nums]

    print('\ninput:', ', '.join(format_nums(nums)))
    print('operations:', ', '.join(operations))
    if not result:
        print('result is empty')
    else:
        print('result:', ', '.join(format_nums(result)))

    while True:
        again = input('again? (y/n): ').strip().lower()

        if again == 'y':
            break_loop = False
            break
        elif again == 'n':
            break_loop = True
            break
        else:
            print('type "y" or "n"\n')

    if break_loop:
        break