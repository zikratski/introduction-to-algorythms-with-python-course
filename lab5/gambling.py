import sys, random, time

def getPlayData(start,goal,n,trials):
	winners_dict = {}
	losers_dict = {}
	players_data = {i:[0,start] for i in range(n)}
	data = {'tries':[0,0],'players':[n,0,0,0],'winners_stats':[0,0,0],
			'losers_stats':[0,0,0],'winners':winners_dict,
			'losers':losers_dict, 'playing':players_data}
	st = time.time()
	for trial in range(trials):
		for i in range(n):
			if i not in winners_dict and i not in losers_dict:
				players_data[i][1] += random.choice([-1,1])
				players_data[i][0] += 1
				if players_data[i][1] >= goal:
					winners_dict[i] = players_data[i]
					del players_data[i]
				elif players_data[i][1] <= 0:
					losers_dict[i] = players_data[i]
					del players_data[i]
		data['tries'][0] +=1
		if n == len(winners_dict) + len(losers_dict):
			break
	end = time.time()
	data['tries'][1] = end - st
	data['players'][1] = len(winners_dict)
	data['players'][2] = len(losers_dict)
	data['players'][3] = len(players_data)
	if not winners_dict:
		data['winners_stats'] = 'no data'
	else:
		wins = [winners_dict[i][0] for i in winners_dict.keys()]
		data['winners_stats'][0] = min(wins)
		data['winners_stats'][1] = sum(wins)/len(wins)
		data['winners_stats'][2] = max(wins)
	if not losers_dict:
		data['losers_stats'] = 'no data'
	else:
		loses = [losers_dict[i][0] for i in losers_dict.keys()]
		data['losers_stats'][0] = min(loses)
		data['losers_stats'][1] = sum(loses)/len(loses)
		data['losers_stats'][2] = max(loses)
	data['winners'] = winners_dict
	data['losers'] = losers_dict
	data['playing'] = players_data
	return data



if __name__ == '__main__':
	start = int(sys.argv[1])
	goal = int(sys.argv[2])
	n = int(sys.argv[3])
	trials = int(sys.argv[4])

	data = getPlayData(start,goal,n,trials)
	print(f"tries: {data['tries'][0]}, time spent: {data['tries'][1]}")
	print(f"total players: {n}, won: {data['players'][1]}, lost: {data['players'][2]}, in progress: {data['players'][3]}")
	print("tries to win: no data") if data['winners_stats'] == 'no data' else print(f"tries to win: min {data['winners_stats'][0]}, avg {data['winners_stats'][1]}, max {data['winners_stats'][2]}")
	print("tries to lose: no data") if data['losers_stats'] == 'no data' else print(f"tries to lose: min {data['losers_stats'][0]}, avg {data['losers_stats'][1]}, max {data['losers_stats'][2]}")
	print(f"won: {data['winners']}")
	print(f"lost: {data['losers']}")
	print(f"in progress: {data['playing']}")



