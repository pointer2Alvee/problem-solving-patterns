""" --------- Top-k Elements ---------"""
# Q : Top k frequent elements (Bucket Sort) 

from collections import Counter

def top_k_frequent(arr, k):
    n = len(arr)
    counter = Counter(arr)
    
    freq_arr = [0] * (n+1) # [1,2,3] => [0, 0, 0, 0], the first 0 is freq 0 

    for num, freq in counter.items():
        if freq_arr[freq] == 0: # if still no elements in that specific idx
            freq_arr[freq] = [num]
            
        else: # Already a list of element(s) in that idx/freq, so append to that list
            freq_arr[freq].append(num)
    
    
    result = []
    for i in range(n, -1, -1):
        if freq_arr[i] != 0:
            result.extend(freq_arr[i]) # freq_arr[i] guranteed to have list of unique numbers
        if len(result) == k:
            break
        
    return result 


my_arr = [1,1,2,2,2,3,3,3,3]
print(f"{top_k_frequent(my_arr,2)}")


""" --------- Top-k Elements ---------"""
# Q : Top k frequent elements (Heap / Min-Heap) 

import heapq # min-heap

def top_k_freq_elms(arr, k):
    counter = Counter(arr)
    heap = []
    
    for key,val in counter.items():
        if len(heap) < k : # we want k items in heap
            heapq.heappush(heap, (val, key))
            
        else: # heap is k things
            heapq.heappushpop(heap, (val, key)) #push something and immediately pop 
 
    return [h[1] for h in heap] # k things, h[1] = key as 1 is 2nd elm



my_arr = [1,1,2,2,2,3,3,3,3,4,4,4,4,4]
print(f"{top_k_freq_elms(my_arr, 2)}")
