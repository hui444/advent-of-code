from collections import defaultdict

f = open("day11/input.txt", "r")
f = f.read().split("\n")
"""
Monkey 0:
  Starting items: 72, 64, 51, 57, 93, 97, 68
  Operation: new = old * 19
  Test: divisible by 17
    If true: throw to monkey 4
    If false: throw to monkey 7


72 * 19
// 3
check test n pass item on
"""

MONKEY_TEXT = "Monkey "
STARTING_ITEMS_TEXT = "  Starting items: "
OPERATION_TEXT = "  Operation: new = old "
TEST_TEXT = "  Test: divisible by "
SUCCESS_TEST = "    If true: throw to monkey "
FAILURE_TEST = "    If false: throw to monkey "

def get_lambda(value, operation):
    if value == "old":
        return lambda x : x ** 2
    if operation == "*":
        return lambda x : x * int(value)
    elif operation == "/":
        return lambda x : x / int(value)
    elif operation == "+":
        return lambda x : x + int(value)
    elif operation == "-":
        return lambda x : x - int(value)

def parser():
    """
    {
        0: {
            items: 72, 64, 51, 57, 93, 97, 68
            operation: new = old * 19
            divide_test: 17
            success: 4
            failure: 7
        }
    }
    """
    monkey_dict = {}
    monkey_num = 0
    curr_items = []
    curr_operation = lambda worry_level : 1 * worry_level
    curr_divide_test = 1
    curr_success_monkey = None
    curr_failure_monkey = None

    for line in f:
        if line.startswith(MONKEY_TEXT):
            monkey_num = int(line[len(MONKEY_TEXT):-1])
        elif line.startswith(STARTING_ITEMS_TEXT):
            curr_items = [int(x) for x in line[len(STARTING_ITEMS_TEXT):].split(", ")]
        elif line.startswith(OPERATION_TEXT):
            operation, value = line[len(OPERATION_TEXT):].split(" ")
            curr_operation = get_lambda(value, operation)
        elif line.startswith(TEST_TEXT):
            curr_divide_test = int(line[len(TEST_TEXT):])
        elif line.startswith(SUCCESS_TEST):
            curr_success_monkey = int(line[len(SUCCESS_TEST):])
        elif line.startswith(FAILURE_TEST):
            curr_failure_monkey = int(line[len(FAILURE_TEST):])
        else:
            monkey_dict[monkey_num] = dict({"items": curr_items, "operation": curr_operation, "divide_test": curr_divide_test, "success": curr_success_monkey, "failure": curr_failure_monkey })

    return monkey_dict

def get_monkey_business_level(num_cycles):
    monkey_dict = parser()
    num_items_inspected_by_monkey = defaultdict(list, { k: 0 for k in range(num_cycles) })
    for _ in range(num_cycles):
        for monkey in monkey_dict.keys():
            monkey_info = monkey_dict[monkey]
            if not monkey_info["items"]:
                continue
            for item in monkey_info["items"]:
                num_items_inspected_by_monkey[monkey] += 1
                new_worry_level = int((monkey_info["operation"])(item)) # // 3
                test_result = new_worry_level % monkey_info["divide_test"]
                new_monkey = monkey_info["success"] if test_result == 0 else monkey_info["failure"]
                monkey_dict[monkey]['items'] = monkey_dict[monkey]['items'][1:]
                monkey_dict[new_monkey]["items"] = monkey_dict[new_monkey]["items"] + [new_worry_level]            
    num_items_inspected = sorted(num_items_inspected_by_monkey.values())

    return num_items_inspected[-1] * num_items_inspected[-2]

print(f"part1: {get_monkey_business_level(20)}")
print(f"part2: {get_monkey_business_level(10000)}")