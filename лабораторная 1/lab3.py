list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

total_players = len(list_players)

mid_point = total_players // 2
team1 = list_players[:mid_point]
team2 = list_players[mid_point:]

print(team1)
print(team2)
