"""Compute the sum of numbers in a list in 3 ways."""

def sum_for(arr):
    arr_sum = 0
    for i in arr:
        arr_sum += i
    return arr_sum

def sum_while(arr):
    arr_sum = 0
    i = 0
    while i < len(arr):
        arr_sum += arr[i]
        i += 1
    return arr_sum

def sum_recursion(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_recursion(arr[1:])

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum_for(arr))
    print(sum_while(arr))
    print(sum_recursion(arr))




if __name__ == '__main__':
    main()