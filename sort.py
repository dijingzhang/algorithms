def bubbleSort(nums):
    """
    O(n^2), O(1), stable
    """
    for i in range(1, len(nums)):
        for j in range(len(nums) - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def selectSort(nums):
    """
    O(n^2), O(1), instable
    """
    for i in range(len(nums) - 1):
        minIndex = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        if i != minIndex:
            nums[minIndex], nums[i] = nums[i], nums[minIndex]
    return nums


def insertSort(nums):
    """
    O(n^2), O(1), stable
    """
    for i in range(len(nums)):
        preIndex = i - 1
        cur = nums[i]
        while preIndex >= 0 and nums[preIndex] > cur:
            nums[preIndex + 1] = nums[preIndex]
            preIndex -= 1
        nums[preIndex + 1] = cur
    return nums


def shellSort(nums):
    """
    O(nlogn), O(1), instable
    """
    import math
    gap = 1
    while gap < len(nums) / 3:
        gap = gap * 3 + 1

    for i in range(gap, len(nums)):
        preIndex = i - gap
        cur = nums[i]
        while preIndex >= 0 and nums[preIndex] > cur:
            nums[preIndex + gap] = nums[preIndex]
            preIndex -= gap
        nums[preIndex + gap] = cur
        gap = math.floor(gap / 3)
    return nums


def mergeSort(nums):
    """
    O(nlogn), O(n), stable
    """
    import math
    if len(nums) < 2:
        return nums
    middle = math.floor(len(nums) / 2)
    left, right = nums[0:middle], nums[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def quickSort(nums, left, right):
    """
    O(nlogn), O(logn), instable
    """
    if left >= right:
        return

    low = left
    high = right
    pivot = nums[left]
    while low < high:
        while low < high and nums[high] >= pivot:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] < pivot:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot
    quickSort(nums, left, low - 1)
    quickSort(nums, low + 1, right)
    return nums


def heapSort(nums):
    """
    O(nlogn), O(1), instable
    """
    for i in reversed(range(len(nums) // 2)):
        sift_down(nums, len(nums), i)

    for i in reversed(range(len(nums))):
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(nums, i, 0)
    return nums

def sift_down(heap, heapSize, root):
    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < heapSize and heap[larger] < heap[left]:
        larger = left
    if right < heapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:
        heap[larger], heap[root] = heap[root], heap[larger]
        sift_down(heap, heapSize, larger)

def countSort(nums, maxValue):
    """
    O(n + k), O(k), stable
    """
    bucketLen = maxValue + 1
    bucket = [0] * bucketLen
    sortedIndex = 0
    n = len(nums)
    for i in range(n):
        if not bucket[nums[i]]:
            bucket[nums[i]] = 0
        bucket[nums[i]] += 1
    for j in range(bucketLen):
        while bucket[j] > 0:
            nums[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return nums


