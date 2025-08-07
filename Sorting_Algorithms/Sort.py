G = [-5, 3, 2, 1, -3, -3, 7, 2, 2,1000]

# In place (constant space)
G.sort()

print(G)

# Get new sorted array - O(n) space

H = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

sorted_H = sorted(H)

H, sorted_H

# Sort array of tuples

I = [(-5, 3), (2, 1), (-3, -3), (7, 2), (2, 2)]

sorted_I = sorted(I, key = lambda t: t[0])

sorted_I
