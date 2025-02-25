import numpy as np

def reshape_matrix(a, new_shape):
    a = np.array(a)
    if a.size != new_shape[0] * new_shape[1]:
        return None
    else:
        return a.reshape(new_shape)
    
a = [[1, 2, 3], [4, 5, 6]]
new_shape = (3, 2)
print(reshape_matrix(a, new_shape))