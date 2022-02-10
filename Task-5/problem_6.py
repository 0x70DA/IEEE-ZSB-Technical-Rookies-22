'''HackerRank: Climbing the Leaderboard'''


def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort()
    for i in player:
        min_index = 0
        max_index = len(ranked)
        while max_index > min_index:
            mid_index = (max_index + min_index) // 2
            if i < ranked[mid_index]:
                max_index = mid_index
            else:
                min_index = mid_index + 1
        print(len(ranked) - min_index + 1)


if __name__ == '__main__':
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    climbingLeaderboard(ranked, player)
