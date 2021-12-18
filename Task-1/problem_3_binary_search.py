"""Implementation of bianry search."""


def binary_search(arr, low, high, value):
    """Retrun the index of the search value if present."""
    if high > low:
        mid = (low + high) // 2
        if value == arr[mid]:
            return mid
        elif value < arr[mid]:
            return binary_search(arr, low, mid-1, value)
        else:
            return binary_search(arr, mid+1, high, value)
    else:
        # Element not in array.
        return None


def main():
    # Prompt user for the array and the search value.
    arr = list(map(int, input('Sorted array (elements seperated by spaces): ').split()))
    value = int(input('Search value: '))
    index = binary_search(arr, 0, len(arr)-1, value)
    if index is not None:
        print(f"Value at index {index}.")
    else:
        print('Value not in array.')


if __name__ == '__main__':
    main()
