def climbingLeaderboard(ranked, player):
    # Write your code here
    ranks = sorted(list(set(ranked)), reverse=True)
    player_ranks = []
    player = sorted(player, reverse=True)
    j = 0
    l = len(ranks)
    
    for i in range(len(player)):
        while j<l and player[i] < ranks[j]:
            j += 1
        player_ranks.append(j + 1)
    return player_ranks[::-1]