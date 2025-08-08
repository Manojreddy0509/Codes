class Node:
  def __init__(self,value):
    self.value=value
    self.next=None

class LinkedList:
  def __init__(self):
    self.head=None

  #O(n) Linear Time
  def print(self):
    if self.head is None:
        return "[]"
    else:
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return "[" + " --< ".join(result) + "]"

  #O(n) Linear Time
  def __contains__(self,value):
    last=self.head
    while last is not None:
      if last.value==value:
        return True
      last=last.next
    return False

  #O(n) Linear Time
  def __length__(self):
    last=self.head
    while last is not None:
      count=0
      last=last.next
    return count

  #O(n) Linear Time
  def append(self,value):
    if self.head is None:
      self.head=Node(value)
    else:
      last=self.head
      while last.next:
        last=last.next
      last.next=Node(value)

  #O(1) Constant Time
  def prepend(self,value):
    first=Node(value)
    first.next=self.head
    self.head=first

  #O(n) Linear Time
  def insert(self,value,index):
    if index==0:
      self.prepend(value)
    else:
      if self.head is None:
        raise Exception("Index out of range")
      else:
        pointer=self.head
        for i in range(index-1):
          if pointer.next is None:
            raise Exception("Index out of range")
          else:
            pointer=pointer.next
        new_node=Node(value)
        new_node.next=pointer.next
        pointer.next=new_node

  #O(n) Linear Time
  def delete(self,value):
    last=self.head
    if last is not None and last.value==value:
        self.head=last.next
        return
    while last is not None and last.next is not None:
      if last.next.value == value:
        last.next = last.next.next
        return
      last = last.next

  #O(n) Linear Time
  def pop(self, index):
    if self.head is None:
        raise Exception("List is empty")
    if index == 0:
        self.head = self.head.next
        return
    last = self.head
    for i in range(index - 1):
        if last is None or last.next is None:
            raise IndexError("Index out of range")
        last = last.next
    if last.next is None:
        raise IndexError("Index out of range")
    last.next = last.next.next


  #O(n) Linear Time
  def get(self, index):
    if self.head is None:
        raise Exception("List is empty")
    last = self.head
    for i in range(index):
        if last is None:
            raise IndexError("Index out of range")
        last = last.next
    if last is None:
        raise IndexError("Index out of range")
    return last.value
if __name__ == "__main__":
  ll=LinkedList()
  ll.append(10)
  ll.append(20)
  ll.append(30)
  ll.append(40)
  ll.prepend(3)
  ll.insert(5,5)
  ll.delete(40)
  ll.pop(1)
  print(ll.get(3))
  print(ll.print())
  print(20 in ll)
  print(200 in ll)






# Singly Linked Lists

class SinglyNode:

  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    return str(self.val)

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)

# Traverse the list - O(n)
curr = Head

while curr:
  print(curr)
  curr = curr.next

# Diplay linked list - O(n)
def display(head):
  curr = head
  elements = []
  while curr:
    elements.append(str(curr.val))
    curr = curr.next
  print(' -> '.join(elements))

display(Head)

# Search for node value - O(n)
def search(head, val):
  curr = head
  while curr:
    if val == curr.val:
      return True
    curr = curr.next

  return False

print(search(Head, 7))

# Doubly Linked Lists

class DoublyNode:
  def __init__(self, val, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev

  def __str__(self):
    return str(self.val)

head = tail = DoublyNode(1)
print(tail)

# Display - O(n)
def display(head):
  curr = head
  elements = []
  while curr:
    elements.append(str(curr.val))
    curr = curr.next
  print(' <-> '.join(elements))

display(head)

# Insert at beginning - O(1)
def insert_at_beginning(head, tail, val):
  new_node = DoublyNode(val, next=head)
  head.prev = new_node
  return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
display(head)

# Insert at end - O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)
