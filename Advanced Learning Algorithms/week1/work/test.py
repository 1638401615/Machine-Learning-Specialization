import numpy as np
a = np.array([[1,2],[2,3]])
b = np.array([1,2])
for j in range(2):
    w = a[:,j]
    print(w)
    ans = np.dot(w,b)
    print("ans:",ans)
