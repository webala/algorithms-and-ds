def acmTeam(topic):
    # Write your code here
    attendees = len(topic)
    max_known_topics = 0
    max_teams = 0
    topics = len(topic[0])
    for i in range(attendees):
        j = i + 1
        while j < topics - 1 and j < attendees:
            team_topics = 0
            team1 = topic[i]
            team2 = topic[j]
            for x in range(topics):
                if team1[x] == 1 and team2[x] == 1:
                    team_topics += 1
            if team_topics > max_known_topics:
                max_known_topics = team_topics
                max_teams = 1
            elif team_topics == max_known_topics:
                max_teams += 1
            j += 1
    return [max_known_topics, max_teams]

topic = ['10101','11110','00010']

print(acmTeam(topic))