def migratoryBirds(arr):
    bird_dict = {}
    for i in range(1, 6):
        bird_dict[i] = 0
    for i in arr:
        bird_dict[i] += 1
    max_sightings = max(bird_dict.values())
    k = [key for key, value in bird_dict.items() if value == max_sightings]
    print(min(k))

# Another solution without using a dictionary.
# def migratoryBirds(arr):
#     ls = [0] * 6
#     for i in arr:
#         ls[i - 1] += 1
#     print(ls.index(max(ls)) + 1)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    migratoryBirds(arr)
