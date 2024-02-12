import numpy as np

m = [2, 3, 4, 5, 6, 7, 8, 9]
print(m[:3])


temp = m[0:5:2]

print(m[::-1])

n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(n[1][2])

p = np.array(n)

print(p[0:2, 0:2], end='\n\n')
print(p[:, :-1], end='\n\n')
print(p[::, -1], end='\n\n')


def test():
    ...
