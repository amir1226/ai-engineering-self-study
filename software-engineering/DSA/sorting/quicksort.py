from DSA.utils.benchmark import time_decorator, benchmark_sort

@time_decorator
def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n//2]
    
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)
    
    return quick_sort(left) + middle + quick_sort(right) 
    
@time_decorator
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p_idx = partition(arr,low,high)
        quick_sort_inplace(arr, low, p_idx-1)
        quick_sort_inplace(arr, p_idx+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low -1 # Pointer for values below pivot
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
    
if __name__ == "__main__":
    benchmark_sort(quick_sort)
    benchmark_sort(quick_sort_inplace)