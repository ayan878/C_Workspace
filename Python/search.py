
# Binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the target is not found

# Example usage
arr = [1, 2, 3, 4, 5, 8, 9]
target = 4

# Binary search
binary_index = binary_search(arr, target)
if binary_index != -1:
    print("Binary search: Element", target, "found at index", binary_index)
else:
    print("Binary search: Element", target, "not found")
