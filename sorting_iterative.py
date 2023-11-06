#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) for a list of n items because we need to make up to n-1 comparisons.
    Memory usage: O(1) because we are not allocating any extra space; checks are done in place."""
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False  # Out of order, return early
    return True  # All in order

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) in the average and worst case because we need to make n-1 passes,
    and each pass requires up to n-1 comparisons/swaps.
    Memory usage: O(1) because sorting is done in place."""
    for i in range(len(items)):
        # Start with the assumption that the list is sorted
        is_sorted = True
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]  # Swap
                is_sorted = False
        if is_sorted:
            break  # No swaps means the list is sorted

def selection_sort(items):
    """Sort given items by finding the minimum item, swapping it with the first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) because we need to make n-1 passes and each pass requires
    scanning n-1 items to find the minimum.
    Memory usage: O(1) because sorting is done in place."""
    for i in range(len(items)):
        # Assume the first unsorted item is the smallest
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j  # Found a new minimum, remember its index
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]  # Swap

def insertion_sort(items):
    """Sort given items by taking the first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2) for average and worst cases because each insertion can take up to O(n) time,
    and we have to do this for n items. However, it runs in O(n) in the best case if the list is already sorted.
    Memory usage: O(1) because sorting is done in place."""
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        # Shift elements of the sorted segment forward if they are larger than the item to insert
        while j >= 0 and current < items[j]:
            items[j + 1] = items[j]
            j -= 1
        # Insert the item
        items[j + 1] = current
