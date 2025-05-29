def prefix_sum(arr, s, e) -> list :
    start, end = s, e
    curr = 0
    prf_sum = []
    
    for i in range(start, end+1):
        curr += arr[i]
        prf_sum.append(curr)

    return prf_sum

my_arr = [1,2,3,4,5,6,7,8,9,10]
print(f"prefix sum : {prefix_sum(my_arr, 0, 5)}")
