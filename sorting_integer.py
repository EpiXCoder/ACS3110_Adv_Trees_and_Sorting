#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) where n is the number of items and k is the range of input.
    Because we're doing a single pass through the numbers, and then another through the range of numbers.
    Memory usage: O(k) because we are creating a list of counts with a size based on the range of the input values."""
    if not numbers:
        return numbers
    
    # Find range of given numbers (minimum and maximum integer values)
    min_num = min(numbers)
    max_num = max(numbers)
    
    # Create list of counts with a slot for each number in input range
    counts = [0] * (max_num - min_num + 1)
    
    # Loop over given numbers and increment each number's count
    for number in numbers:
        counts[number - min_num] += 1
    
    # Loop over counts and append that many numbers into output list
    index = 0
    for number, count in enumerate(counts):
        while count > 0:
            numbers[index] = number + min_num
            index += 1
            count -= 1
    return numbers

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n + k) on average if the numbers are uniformly distributed. In the worst case, can degrade to O(n^2) if all numbers are in the same bucket.
    The k represents the number of buckets, and the sorting of each bucket takes O(n/k * log(n/k)) time.
    Memory usage: O(n + k) because we are creating k buckets and potentially storing a copy of n input numbers across these buckets."""
    if not numbers:
        return numbers
    
    # Find range of given numbers (minimum and maximum values)
    min_num = min(numbers)
    max_num = max(numbers)
    range_num = max_num - min_num
    
    # Create list of buckets to store numbers in subranges of input range
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute input numbers into the buckets
    for number in numbers:
        # Place each number in appropriate bucket
        index = (number - min_num) * num_buckets // (range_num + 1)
        buckets[index].append(number)
    
    # Sort each bucket and concatenate the results
    sorted_numbers = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket)  # Here we use any sorting algorithm, often recursive
        sorted_numbers.extend(sorted_bucket)
    
    # Copy the sorted numbers back into the original list
    for i, num in enumerate(sorted_numbers):
        numbers[i] = num
    
    return numbers
