def max_sum_subarray(arr, k):
    # Calculate the sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window from start to end of the array
    for i in range(len(arr) - k):
        # Update the window sum by subtracting the element that is left behind
        # and adding the new element that comes into the window
        window_sum = window_sum - arr[i] + arr[i + k]
        # Update the maximum sum if the current window sum is greater
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print("Maximum sum of subarray of size", k, "is", max_sum_subarray(arr, k))