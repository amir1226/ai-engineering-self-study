from functools import wraps
from time import perf_counter_ns
import random
import tracemalloc

not_in_place_sorts = {"quick_sort", "merge_sort"}

def time_decorator(func):
    is_running = False
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal is_running
        root_call = not is_running
        
        if root_call:
            is_running = True
            tracemalloc.start()
            start_time = perf_counter_ns()
            result = func(*args, **kwargs)
            end_time = perf_counter_ns()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(f"Execution time: {(end_time - start_time) / 1e6:.4f} ms")
            print(f"peak memory: {peak / 1024:.2f} KB")
            is_running = False
        else:
            result = func(*args, **kwargs)
        return result
    return wrapper

def validate_sort(sort_fn, arr, name="list"):
    expected = sorted(arr)
    if sort_fn.__name__ in not_in_place_sorts:
        arr = sort_fn(arr)
    else:
        sort_fn(arr)
    print(f"{name} sorted: {'OK' if arr == expected else 'FAILED'}")
    

def benchmark_sort(sort_fn):
    random.seed(12)
    print(
        "-" * 40,
        "\n", 
        f"Benchmarking sort function '{sort_fn.__name__}'",
        "\n",
        "-" * 40
    )
    test_cases = {
        "small": [random.randint(-200, 200) for _ in range(100)],
        "medium": random.sample(range(10_000), 1_000),
        "big": random.sample(range(100_000), 10_000),
    }

    for name, arr in test_cases.items():
        validate_sort(sort_fn, arr, name)