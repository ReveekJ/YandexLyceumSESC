import math


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, *values):
        for elem in values:
            self.__stack.append(elem)

    def pop(self, times: int = 1):
        for i in range(times):
            self.__stack.pop()

    def get_last_one(self):
        return self.__stack[-1]

    def get_last_two(self):
        return self.__stack[-2:]

    def get_last_three(self):
        return self.__stack[-3:]


inp = input().split()
stack = Stack()

for i in inp:
    if i.isdigit():
        stack.push(int(i))
        continue

    match i:
        case '+':
            nums = stack.get_last_two()
            stack.pop(2)
            stack.push(sum(nums))
        case '-':
            nums = stack.get_last_two()
            stack.pop(2)
            stack.push(nums[0] - nums[1])
        case '*':
            nums = stack.get_last_two()
            stack.pop(2)
            stack.push(nums[0] * nums[1])
        case '/':
            nums = stack.get_last_two()
            stack.pop(2)
            stack.push(nums[0] // nums[1])
        case '~':
            num = stack.get_last_one()
            stack.pop()
            stack.push(-num)
        case '!':
            num = stack.get_last_one()
            stack.pop()
            stack.push(math.factorial(num))
        case '#':
            num = stack.get_last_one()
            stack.push(num)
        case '@':
            nums = stack.get_last_three()
            stack.pop(3)
            stack.push(nums[1], nums[2], nums[0])

print(stack.get_last_one())
