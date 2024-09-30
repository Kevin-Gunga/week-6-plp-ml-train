# properties:
#1.Homogeneous data type: All elements of a NumPy array must have the same data type, which is typically a numeric data type such as int or float.
#2.Fixed size: The size of a NumPy array is fixed when it is created, and it cannot be changed without creating a new array.
#3.Efficient: NumPy arrays are designed to be efficient for numerical operations, and they are implemented in C, which makes them faster than Python lists.

import numpy as np

# a = np.array([1, 2, 3])
# print(a)

# 2D NumPy array:
import numpy as np
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# Using NumPy functions to perform mathematical operations on arrays:
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# addition 
print(a + b)

# sub
print(a-b)

# mult
print(a * b)

# div
print(b/a)

# Slicing and indexing NumPy arrays:
import numpy as np
a = np.array([1,2,3,4,5])
print(a[0])
print(a[1:4])

# Reshaping NumPy arrays:
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
b = a.reshape((3,3))
print(b)