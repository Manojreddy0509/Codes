# SELECTION SORT

#Time Complexity : O(n^2)
#Space Complexity :O(1)

def selection_sort(arr):
  n=len(arr)
  for i in range(n):
    min_index=i
    for j in range(i+1,n):
      if arr[j]<arr[min_index]:
        min_index=j
    arr[i], arr[min_index] = arr[min_index], arr[i]

C=[-5,3,2,2,4,-2,1,-3,-3,7,2,2,1]
selection_sort(C)
C
