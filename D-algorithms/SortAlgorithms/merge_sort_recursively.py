def merge_sort(array):
    # Base case: If array has 0 or 1 element, it is already sorted
    if len(array) <= 1:
        return array

    # Recursive case: Split the array into halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursive calls to sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0

    # Merge process
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # Append any remaining elements from left or right
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array

# Example usage:
array = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", array)
sorted_array = merge_sort(array)
print("Sorted array:", sorted_array)
