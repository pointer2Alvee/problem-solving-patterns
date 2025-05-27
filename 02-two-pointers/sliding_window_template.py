""" --------- Fixed Size Window ---------"""
# Q : Find the max sum of the subarray 
def max_sum_subarray(arr,k):
    curr = best = sum(arr[0:k])
    
    for i in range(k, len(arr)):
        curr = curr + arr[i] - arr[i-k]
        best = max(curr, best)
        
    return best

my_arr = [8,3,-2,4,5,-1,0,5,3,9,-6]
print(f"Max sum Subarray : {max_sum_subarray(my_arr, 5)}")



""" --------- Variable Size Window ---------"""
# Q : Find the max sum of the subarray 

