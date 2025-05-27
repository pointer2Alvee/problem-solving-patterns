# Q : Given arr = [-4,-1,0,3,10], Return its square in aescending order

def sorted_squared(arr) -> list :
    
    # two pointers 
    left = 0 
    right = len(arr)-1
    
    # place in the last idx 
    pos = len(arr)-1 
    array  = [0] * len(arr)
    
    while left <= right:
        if abs(arr[left]) < abs(arr[right]):
            array[pos] = arr[right]**2 
            right -= 1
        else:
            array[pos] = arr[left]**2
            left += 1
        pos -= 1
        
    return array


arr = [-4,-1,0,3,10]
print(f"Sorted Squared :- {sorted_squared(arr)}")

















