# QUICK SORT

#Time Complexity : Best : O(n logn) Average : O(n logn) Worst : O(n^2)
#Space Complexity :

def quick_sort(arr):
  n=len(arr)
  if n<=1:
    return arr

  pivot=arr[0]
  L,R=[],[]

  for i in range(1,n):
    if arr[i]>pivot:
      R.append(arr[i])
    else:
      L.append(arr[i])

  return quick_sort(L)+[pivot]+quick_sort(R)

E=[-5,3,2,2,4,-2,1,-3,-3,7,2,2,1]
quick_sort(E)
