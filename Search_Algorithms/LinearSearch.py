# LINEAR SEARCH

#Time Complexity : O(N)

def linear_search(arr,target):
  for i in range(len(arr)):
    if arr[i]==target:
      return True
  return False

x=[-5,3,2,1,-3,-3,7,2,2,100]
linear_search(x,5)
