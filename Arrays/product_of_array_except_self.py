def product(arr):
    product = 1
    for element in arr:
        product *= element
    return product

arr  = [ 1,2,3]
print(product(arr)) # 6
        
        