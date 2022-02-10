'''Build Max Heap'''


def left(i, arr):
    """Return the index of the left child."""
    l = (2 * i) + 1
    return l if l <= len(arr) else None


def right(i, arr):
    """Return the index of the right child."""
    r = (2 * i) + 2
    return r if r <= len(arr) else None


def max_heapify(arr, i):
    l = left(i, arr)
    r = right(i, arr)
    if l is None or r is None:
        return
    largest = l if l <= len(arr) and arr[l] > arr[i] else i
    largest = r if r <= len(arr) and arr[r] > arr[largest] else largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


def build_max_heap(arr):
    for i in range(len(arr)//2, -1, -1):
        max_heapify(arr, i)


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    build_max_heap(arr)
    print(*arr)
