with open('./day_2_1.txt') as f:
	lines = f.readlines()
	score = 0

	opp_map = {
		'A': 'rock',
		'B': 'paper',
		'C': 'scissors'
	}
	player_map = {
		'X': 'rock',
		'Y': 'paper',
		'Z': 'scissors'
	}

	game_scenarios = {
		'rock': {
			'rock': 'tie',
			'paper': 'win',
			'scissors': 'lose'
		},
		'paper': {
			'rock': 'lose',
			'paper': 'tie',
			'scissors': 'win'
		},
		'scissors': {
			'rock': 'win',
			'paper': 'lose',
			'scissors': 'tie'
		}
	}
	for line in lines:
		play = line.strip().split(' ')
		outcome = game_scenarios[opp_map[play[0]]][player_map[play[1]]]
		
		player_score = (ord(play[1]) - ord('X') + 1)

		if outcome == 'win':
			score += 6 + player_score
		elif outcome == 'lose':
			score += player_score
		else:
			score += 3 + player_score
		#print(outcome)
		
	print(score)
