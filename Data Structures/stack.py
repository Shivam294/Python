# stack = []

# def push(val):
#     stack.append(val)

# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val

# push(3)
# push(2)
# push(1)
# print(stack)
# print(pop())
# print(pop())
# print(pop())
class Stack:
    def __init__(self):
        # self.__stack_list= []  //Private
        self.stack_list = []

    def push(self, val):
        self.stack_list.append(val)
        # self.__stack_list.append (val)

    def pop(self):
        val = self.stack_list[-1]
        del self.stack_list[-1]
        return val

stack_object = Stack()
# print(len(stack_object.__stack_list))  //Private
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(len(stack_object.stack_list))

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())