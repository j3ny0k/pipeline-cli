def even(nums):
    return [x for x in nums if x % 2 == 0]


def odd(nums):
    return [x for x in nums if x % 2 != 0]


def double(nums):
    return [x * 2 for x in nums]


def square(nums):
    return [x**2 for x in nums]


def sort(nums):
    return sorted(nums)


ops = {"even": even, "odd": odd, "double": double, "square": square, "sort": sort}


def format_nums(nums):
    return [str(x) for x in nums]


def parse_nums():
    while True:
        raw = input("\nnums: ").strip()

        if not raw:
            print("input is empty")
            continue

        try:
            return [int(x) for x in raw.split()]
        except ValueError:
            print("only integers allowed")


def parse_operations(ops):
    while True:
        raw = input("\noperations: ").strip()

        if not raw:
            print("input is empty")
            continue

        elif raw == "help":
            print("available operations:", ", ".join(ops))
            continue

        operations = raw.split()

        invalid = [name for name in operations if name not in ops]

        if invalid:
            print("invalid operations:", ", ".join(invalid))
            print("available:", ", ".join(ops))
            continue

        return operations


print("type help to show available operations")
print("enter numbers separated by space (example: 1 2 3)")
print("enter operations separated by space (example: even double)")

while True:
    nums = parse_nums()

    operations = parse_operations(ops)
    result = nums

    for name in operations:
        result = ops[name](result)

    print("input:", ", ".join(format_nums(nums)))
    print("operations:", ", ".join(operations))

    if not result:
        print("result is empty")

    else:
        print("result:", ", ".join(format_nums(result)))

    while True:
        again = input("\nagain? (y/n): ").strip().lower()

        if again == "y":
            break_loop = False
            break

        elif again == "n":
            break_loop = True
            break

        else:
            print("type y or n")

    if break_loop:
        break
