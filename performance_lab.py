# Problem 1: Find Most Frequent Element

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    return max(counts, key=counts.get)


"""
Time and Space Analysis for problem 1:
- Best-case: O(n).
- Worst-case: O(n^2) with extreme hash collisions; normally O(n).
- Average-case: O(n).
- Space complexity: O(n) for the dictionary of counts.
- Why this approach? Counts each number in one pass.
- Could it be optimized? It already takes linear time on average.
  Sorting could avoid hash collisions, but takes O(n log n) time.
  Empty input returns None.
"""


# Problem 2: Remove Duplicates While Preserving Order

def remove_duplicates(nums):
    seen = set()
    result = []

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


"""
Time and Space Analysis for problem 2:
- Best-case: O(n).
- Worst-case: O(n^2) with extreme hash collisions; normally O(n).
- Average-case: O(n).
- Space complexity: O(n) for the set and output list.
- Why this approach? The set checks duplicates quickly, while
  the result list preserves the original order.
- Could it be optimized? Checking only the result list removes
  the extra set, but can take O(n^2) time.
"""


# Problem 3: Return All Pairs That Sum to Target
# The input has no duplicates, as specified in the assignment.

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for number in nums:
        needed = target - number

        if needed in seen:
            pairs.append((needed, number))

        seen.add(number)

    return pairs


"""
Time and Space Analysis for problem 3:
- Best-case: O(n).
- Worst-case: O(n^2) with extreme hash collisions; normally O(n).
- Average-case: O(n).
- Space complexity: O(n) for the set and output pairs.
- Why this approach? Finds matching numbers in one pass.
  Each pair is added only when its second number is reached.
- Could it be optimized? Sorting and using two pointers avoids
  the set but takes O(n log n) time. Sorting in place changes
  the input; sorting a copy requires extra space.
"""


# Problem 4: Simulate List Resizing

def add_n_items(n):
    capacity = 2
    items = [None] * capacity
    size = 0

    for number in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print(f"Resizing from {capacity} to {new_capacity}")

            new_items = [None] * new_capacity

            for index in range(size):
                new_items[index] = items[index]

            items = new_items
            capacity = new_capacity

        items[size] = number
        size += 1

    return items[:size]


"""
Time and Space Analysis for problem 4:
- When do resizes happen? Before adding an item when the current
  list is full: at sizes 2, 4, 8, 16, and so on.
- Worst-case for a single append: O(k), where k is the number
  of existing items that must be copied.
- Amortized time per append: O(1).
- Total time: O(n) for n additions, including the final slice.
- Space complexity: O(n) for the lists, including temporary
  storage during resizing.
- Why does doubling reduce the cost overall? Copies happen
  less frequently as capacity grows. The total number of
  copied items is less than 2n.
- Trade-off: Unused capacity takes extra memory.
  The function stores the integers 0 through n - 1.
"""


# Problem 5: Compute Running Totals
# Original version kept for the optimization comparison.

def running_total_original(nums):
    result = []

    for index in range(len(nums)):
        result.append(sum(nums[:index + 1]))

    return result


"""
Analysis of the original version:
- Best-case, worst-case, and average-case: O(n^2).
- Space complexity: O(n), including the output and temporary slices.
- Repeatedly copies and sums prefixes of the input.
"""


def running_total(nums):
    # Optimization: Keep a running sum instead of repeatedly
    # slicing and summing. Time improves from O(n^2) to O(n).
    # Both versions use O(n) total space, but this version uses
    # O(1) auxiliary space beyond the output and creates no slices.

    result = []
    total = 0

    for number in nums:
        total += number
        result.append(total)

    return result


"""
Time and Space Analysis for problem 5:
- Best-case: O(n).
- Worst-case: O(n).
- Average-case: O(n).
- Space complexity: O(n) for the output; O(1) auxiliary space.
- Why this approach? Visits each number once and reuses the total.
- Could it be optimized? Updating the input in place could avoid
  the new output list, but would change the caller's original data.
"""


# Tests

if __name__ == "__main__":
    # Problem 1
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
    assert most_frequent([]) is None
    assert most_frequent([7]) == 7
    assert most_frequent([1, 1, 2, 2]) in (1, 2)
    assert most_frequent([-2, -2, 0]) == -2

    # Problem 2
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([]) == []
    assert remove_duplicates([2, 2, 2]) == [2]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([-1, 0, -1]) == [-1, 0]

    # Problem 3: Normalize pairs because output order does not matter.
    assert {
        tuple(sorted(pair))
        for pair in find_pairs([1, 2, 3, 4], 5)
    } == {(1, 4), (2, 3)}
    assert find_pairs([], 5) == []
    assert find_pairs([1], 2) == []
    assert find_pairs([1, 2, 3], 10) == []
    assert find_pairs([-3, 0, 3], 0) == [(-3, 3)]

    # Problem 4: Check returned values and resizing messages.
    from contextlib import redirect_stdout
    from io import StringIO

    output = StringIO()
    with redirect_stdout(output):
        assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

    assert output.getvalue().splitlines() == [
        "Resizing from 2
