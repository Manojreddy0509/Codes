# MERGE SORT

#Time Complexity : O(n logn)
#Space Complexity :O(n)

def merge_sort(arr):
  n=len(arr)

  if n==1:
    return arr

  mid=n//2
  L=arr[:mid]
  R=arr[mid:]

  L=merge_sort(L)
  R=merge_sort(R)

  L_len=len(L)
  R_len=len(R)
  l,r,i=0,0,0
  sorted_arr=[0]*n

  while l<L_len and r<R_len:
    if L[l]<R[r]:
      sorted_arr[i]=L[l]
      l+=1
    else:
      sorted_arr[i]=R[r]
      r+=1
    i+=1

  while l<L_len:
    sorted_arr[i]=L[l]
    i+=1
    l+=1

  while r<R_len:
    sorted_arr[i]=R[r]
    i+=1
    r+=1

  return sorted_arr

D=[-5,3,2,2,4,-2,1,-3,-3,7,2,2,1]
merge_sort(D)
