from DSA.utils.benchmark import time_decorator, benchmark_search

@time_decorator
def binary_search_recursive(arr, target, left=0, right=None):
    n= len(arr)
    if right is None:
        right = n-1   
    if left > right:
        return -1
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target,left,mid-1)
    else:
        return binary_search_recursive(arr, target,mid+1, right)

@time_decorator
def binary_search_iterative(arr, target):
    i = 0
    j = len(arr)-1
    while i<=j:
        mid = (i+j)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return -1
    

if __name__ == "__main__":
    benchmark_search(binary_search_recursive, binary_search_iterative)