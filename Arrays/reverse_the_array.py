def reverse_array(arr):
    reverse_array =  arr[::-1]
    
    print("Original Array: ", arr)
    print("Reversed Array: ", reverse_array)
    for i in reverse_array:
        print(i, end=" ")
        
def reverse_the_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
arr = [1, 2, 3, 4, 5]
reverse_array(arr)


        

