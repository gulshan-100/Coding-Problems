from itertools import permutations

def permu(str):
    perm = permutations(str)
    unique_perm = sorted(set([''.join(p) for p in perm]))
    return unique_perm
        
string = "ABC"
print(permu(string))
