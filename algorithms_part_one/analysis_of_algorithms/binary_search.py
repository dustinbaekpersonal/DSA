"""Binary search algorithm in Python."""

def binary_search(array: list, num: int) -> bool:
    """Find a number exists in array or not.
    
    Conditions:
    1. array should be already sorted
    2. if num exists return True, if not False
    
    e.g. array = [1, 3, 6, 10, 30], num = 3
    
    """
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        # mid = int(lo + (hi - lo) / 2)
        print(mid)
        if array[mid] < num:
            lo = mid + 1
        elif array[mid] > num:
            hi = mid - 1
        else:
            return True
    return False


array = [1, 3, 6, 10, 30]
num = 2
 
res = binary_search(array, num)
print(res)