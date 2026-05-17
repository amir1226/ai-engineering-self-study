from DSA.utils import time_decorator, benchmark_sort

@time_decorator
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left,right)

def merge(left, right):
    n, m = len(left),len(right)
    result = []
    i ,j = 0,0
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
    
if __name__ == "__main__":
    benchmark_sort(merge_sort)
