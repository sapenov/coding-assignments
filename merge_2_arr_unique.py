# Merging of two arrays into one with unique elements

# Case 1 - most values repeat, prefer dedupe first, then sort.
# Cost of dedupe is O(n), sort O(n log(n/10)).

# Case 2 - most values are unique, prefer combine sorting and deduping.
# Cost of dedupe is O(n), sort O(n log(n)).

# case 3 - values are half unique, sort and dedupe.
# Cost of dedupe is O(n/2), sort O(n log(n/2)).

def msort(arr):
    l = len(arr)
    if l > 1:
        mid = l//2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        msort(left)
        msort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                arr[k] = left[i]

                # Move the iterator forward
                i +=1
            else:
                arr[k] = right[j]
                j +=1
            # Move to the next slot
            k+=1

        # For all the remaining values
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1


a = [23, 67, 1,1,2,2,2, 4, 29,48, 9,29,23]
a = list(set(a))
print(f"Unsorted list is {a}")

msort(a)

print(f"Sorted list with unique elements is {a}")
