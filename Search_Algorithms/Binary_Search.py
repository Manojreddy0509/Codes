# BINARY SEARCH

#Time Complexity : O(logn)
#Space Complexity :O(1)

def binary_search(arr,target):
  n=len(arr)
  l,r=0,n-1

  while l<=r:
    m=l+((r-l)//2)
    if arr[m]==target:
      return True
    elif arr[m]<target:
      l=m+1
    else:
      r=m-1
  return False

A=[-3,2,5,9,10,27]
binary_search(A,5)
