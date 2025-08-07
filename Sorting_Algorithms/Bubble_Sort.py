# BUBBLE SORT

#Time Complexity : O(n^2)
#Space Complexity :O(1)

def bubblesort(arr):
  n = len(arr)
  flag=True
  while flag:
    flag=False
    for i in range(1, n):
      if arr[i] < arr[i-1]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        flag=True

A=[-5,3,2,1,-3,-3,7,2,2,100]
bubblesort(A)
A
