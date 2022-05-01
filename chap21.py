# 1
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
for c in "позавчера":
    stack.push(c)

reverse = ""

for i in range(stack.size()):
    reverse += stack.pop()

print(reverse)

# 2
list = [1, 2, 3, 4, 5]
stack_list = Stack()
for c in list:
    stack_list.push(c)

reverse_list = []

for i in range(stack_list.size()):
    reverse_list.append(stack_list.pop())

print(reverse_list)