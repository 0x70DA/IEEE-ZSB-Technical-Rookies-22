def main():
    arr = []
    for _ in range(int(input())):
        arr.append([*list(map(int, input().split()))])
    volume_sum = sum([row[0] for row in arr])
    # Get the list of bottels' capacities.
    capacities = [row[1] for row in arr]
    # Get the sum of the two max capacities.
    max_capacity = 0
    for _ in range(2):
        max_capacity += max(capacities)
        capacities.remove(max(capacities))
    if volume_sum <= max_capacity:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
