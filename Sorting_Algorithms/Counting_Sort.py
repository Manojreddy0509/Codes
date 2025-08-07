# COUNTING SORT

# Time Complexity : O(n+k) k=range of data
# Space Complexity : O(k)

def counting_sort(arr):
  n=len(arr)
  maxx=max(arr)
  counts=[0]*(maxx+1)

  for num in arr:
    counts[num]+=1

  i=0
  for c in range(len(counts)):
    while counts[c]>0:
        arr[i]=c
        i+=1
        counts[c]-=1
  return arr

F=[5,3,2,1,3,3,7,2,2]
counting_sort(F)
