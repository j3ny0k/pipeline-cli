print('available operations: even, odd, double, square')
print('enter operations using "_" (example: even_double)\n')

def even(nums):
    return [x for x in nums if x % 2 == 0]
def odd(nums):
    return [x for x in nums if x % 2 != 0]
def double(nums):
    return [x * 2 for x in nums]
def square(nums):
    return [x ** 2 for x in nums]

ops = {
    'even': even,
    'odd': odd,
    'double': double,
    'square': square
}

def parse_nums():
    while True:
        raw = input("nums: ").strip()

        if not raw:
            print("empty input\n")
            continue

        try:
            return [int(x) for x in raw.split()]
        except ValueError:
            print("only integers allowed\n")

nums = parse_nums()

def parse_operations(ops):
    while True:
        raw = input("\noperations: ").strip()

        if not raw:
            print("no operations")
            continue

        operations = raw.split("_")

        invalid = [name for name in operations if name not in ops]

        if invalid:
            print("invalid operations:", ", ".join(invalid))
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
print('result:', ', '.join(format_nums(result)))