#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n + m) where n and m are lengths of items1 and items2.
    Memory usage: O(n + m) for the new merged list."""
    merged = []
    i, j = 0, 0
    while i < len(items1) and j < len(items2):
        if items1[i] < items2[j]:
            merged.append(items1[i])
            i += 1
        else:
            merged.append(items2[j])
            j += 1
    merged.extend(items1[i:])
    merged.extend(items2[j:])
    return merged
    
def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(n log n) since each split divides the list and each merge is linear.
    Memory usage: O(n) due to the additional lists created for merging."""
    if len(items) <= 1:
        return items
    middle = len(items) // 2
    left = split_sort_merge(items[:middle])
    right = split_sort_merge(items[middle:])
    return merge(left, right)

    
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n log n) as the list is repeatedly split and merged.
    Memory usage: O(n) for the temporary lists used in merging."""
    if len(items) <= 1:
        return items
    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    return merge(left, right)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(n) where n is the number of elements in range.
    Memory usage: O(1) as partitioning is done in place."""
    pivot = items[high]
    i = low - 1
    for j in range(low, high):
        if items[j] < pivot:
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[high] = items[high], items[i + 1]
    return i + 1


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
Best case running time: O(n log n) when partitions are balanced.
    Worst case running time: O(n^2) when partitions are unbalanced.
    Memory usage: O(log n) for recursive call stack in best case, O(n) in worst case."""
    if high is None:
        high = len(items) - 1
    if low < high:
        pivot_index = partition(items, low, high)
        quick_sort(items, low, pivot_index - 1)
        quick_sort(items, pivot_index + 1, high)