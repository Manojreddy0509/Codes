import heapq
def HeapSort(arr):
    heapq.heapify(arr)
    n=len(arr)
    new=[0]*n
    for i in range(n):
        minn=heapq.heappop(arr)
        new[i]=minn
    print(new)
HeapSort([2,8,9,0,3,7,4,6])
