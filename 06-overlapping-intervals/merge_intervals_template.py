""" --------- Overlapping Intervals ---------"""
# Q : Merge Overalpping Intervals 

def merge(intervals) -> list:
    # sort intervals array by their starting points / first component 
    intervals.sort(key = lambda interval : interval[0])
    merged = []
    
    for interval in intervals:
        """
        merged[-1][1] = [-1] last item in merged arr, 
        [-1][1] = 2nd component of last item in merged arr
        
        => overlap condition :- x[1] ≥ y[0], no overlap cond :  x[1] < y[0]
        => In code, no overlap cond:- merged[-1][1] < interval[0]
        
        x[1] == merged[-1][1] 
        y[0] == interval[0]
        
        max(merged[-1][1], interval[1]) => take max between max(1st_end,2nd_end)
        """
        if not merged or merged[-1][1] < interval[0]:  # if no overlap
            merged.append(interval)
        
        else : # if overlap
            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        
    return merged
    
    # time : O(nlogn) , space : O(n)
    

arr = [[2,6],[1,3],[8,10],[7,9]]
print(f"{merge(arr)}")