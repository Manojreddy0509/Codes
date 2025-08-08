# STACKS (Last In First Out) LIFO

stk=[]

# Append to top of Stack - O(1)
stk.append(10)
stk.append(20)
stk.append(30)
print(stk)

# Pop from stack - O(1)
x=stk.pop()
print(x)
print(stk)

# Peek (Top of stack) - O(1)
print(stk[-1])

# Checks if the stack is Empty or not -O(1)
if stk:
  print("Stack is not Empty")
else:
  print("Stack is Empty")





# Queues (First In First Out) FIFO

from collections import deque
q=deque()
print(q)

# Enqueue - (Add Element to Right) - O(1)

q.append(10)
q.append(20)
q.append(30)
print(q)

# Dequeue - Popleft()- (Remove Element from Left) - O(1)
x=q.popleft()
print(x)
print(q)

# Peek from Left side - O(1)
print(q[0])

# Peek from Right side - O(1)
print(q[-1])
