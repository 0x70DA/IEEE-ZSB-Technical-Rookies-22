'''HackerRank: ACM ICPC Team'''
from math import ceil, log2


def acmTeam(topics, n):
    arr = [bin(int(topics[i], 2) | int(topics[j], 2))[2:].count('1') for i in range(n) for j in range(i+1, n)]
    max_score = max(arr)
    print(max_score, arr.count(max_score), sep='\n')


if __name__ == '__main__':
    n, m = map(int, input().split())
    topics = [input() for _ in range(n)]
    acmTeam(topics, n)
