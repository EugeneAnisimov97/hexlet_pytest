stack = []  # В Python стек реализован через список
not stack  # Список пуст
# True
stack.append(1)  # [1]
stack.append(2)  # [1, 2]
stack.append(3)  # [1, 2, 3]
print(not stack)
print(stack)
stack.pop() 
stack.pop()
stack.pop()
print(not stack)