# Condition based
B = [False, False, False, False, True]

def binary_search_condition(arr):
  N = len(arr)
  L = 0
  R = N - 1

  while L < R:
    M = (L + R) // 2

    if arr[M]:
      R = M
    else:
      L = M + 1

  return L

binary_search_condition(B)
