import numpy as np

# Create a 3x3 array of random integers between 1 and 100 inclusive
a = np.random.randint(1, 101, size=(3,3))

# Calculate the total sum of all elements in the array
total_sum = np.sum(a)

# Find the maximum and minimum values in the array along with their indexes
max_value = np.max(a)
max_value_index = np.unravel_index(np.argmax(a), a.shape)
min_value = np.min(a)
min_value_index = np.unravel_index(np.argmin(a), a.shape)

# Sort the array by each row
a_sorted = np.sort(a, axis=1)


# Print the results
print("Original Array:\n", a)
print("\nTotal Sum:", total_sum)
print("\nMaximum Value:", max_value, "with index", max_value_index)
print("\nMinimum Value:", min_value, "with index", min_value_index)
print("\nSorted Array by Row:\n", a_sorted)