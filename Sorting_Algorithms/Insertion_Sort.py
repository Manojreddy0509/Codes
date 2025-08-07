# INSERTION SORT

#Time Complexity : O(n^2)
#Space Complexity :O(1)

def insertion_sort(arr):
  n=len(arr)
  for i in range(1,n):
    for j in range(i,0,-1):
      if arr[j-1]>arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
      else:
        break

B=[-5,3,2,2,4,-2,1,-3,-3,7,2,2,1]
insertion_sort(B)
B
