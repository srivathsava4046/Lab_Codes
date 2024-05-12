import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)  # Choose a random pivot element
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)

# Example usage:
arr = [3, 6, 8, 4, 10, 1, 2, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
