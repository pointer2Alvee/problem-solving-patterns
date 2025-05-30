""" --------- Monotonic Stack ---------"""
# Q : Next Greater Element ( decreasing stack ) 

def next_greater_element(arr) -> list:
    result = [-1] * len(arr)
    stk = []  # Stack to store indices

    for idx in range(len(arr)):
        while stk and arr[idx] > arr[stk[-1]]: # stk[-1] == pop() last element, here elements are indices
            prev_idx = stk.pop()
            result[prev_idx] = arr[idx]
        stk.append(idx)

    return result

arr = [2, 1, 5, 6, 2, 3]
print(f"Next Greater Elements: {next_greater_element(arr)}")

""" --------- Monotonic Stack ---------"""
# Q : Next smaller Element ( Increasing stack ) 
def next_smaller_element(arr) -> list:
    result = [-1] * len(arr)
    stk = []  # Stack to store indices

    for idx in range(len(arr)):
        while stk and arr[idx] < arr[stk[-1]]:
            prev_idx = stk.pop()
            result[prev_idx] = arr[idx]
        stk.append(idx)

    return result

arr = [2, 1, 5, 6, 2, 3]
print(f"Next Smaller Elements: {next_smaller_element(arr)}")


"""** my attempt:- ** almost correct
# --------- Monotonic Stack ---------
# Q : Next Greater Element ( decreasing stack ) 

def next_greater_element(arr) -> list: 
    result = [-1] * len(arr)
    stk = []
    
    for idx in range(len(arr)+1):
        while stk is not []:
            if arr[idx] > arr[stk[-1]]: 
                result[stk[-1]] = arr[idx]
                stk.pop()
                if stk is []:
                    stk.append(idx)
                    break
            else: 
                stk.append(idx)
  
        
        else:
            stk.append(idx)


    return result
            

arr = [2,1,5,6,2,3]
print(f"{next_greater_element(arr)}")

"""