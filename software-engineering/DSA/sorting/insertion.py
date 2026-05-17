from DSA.utils import time_decorator, benchmark_sort

@time_decorator
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i-1
        current = arr[i]
        
        while j >= 0 and current < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current

    return arr                 

if __name__ == "__main__":
    benchmark_sort(insertion_sort)
    