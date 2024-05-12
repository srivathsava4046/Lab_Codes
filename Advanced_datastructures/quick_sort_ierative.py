def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Create an explicit stack to simulate recursion
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            # Partition the array
            pivot = partition(arr, low, high)

            # Push subarrays onto the stack
            stack.append((low, pivot - 1))
            stack.append((pivot + 1, high))

    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
