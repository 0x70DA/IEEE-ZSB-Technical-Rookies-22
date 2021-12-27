def breakingRecords(scores):
    # Write your code here
    highest_score = lowest_score = scores[0]
    count_max = 0
    count_min = 0
    for i in range(1, len(scores)):
        if scores[i] > highest_score:
            highest_score = scores[i]
            count_max += 1
        elif scores[i] < lowest_score:
            lowest_score = scores[i]
            count_min += 1
    return [count_max, count_min]


if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    print(breakingRecords(scores))
