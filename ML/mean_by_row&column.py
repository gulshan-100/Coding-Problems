import numpy as np                              

def mean_by_row_column(a, mode):
    a = np.array(a)
    if mode == 'row':
        return np.mean(a, axis=1)
    elif mode == 'column':
        return np.mean(a, axis=0)
    else:
        return None
    
a = [[1, 2, 3], [4, 5, 6]]
print(mean_by_row_column(a, 'row'))
print(mean_by_row_column(a, 'column'))
    