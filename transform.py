import json


def load_indicators(filepath='jewish_indicators.json'):
	# getting the "jewish filters"
	with open(filepath, 'r', encoding='utf-8') as f:
		return json.load(f)


def calculate_jewish_probability(player, indicators):
	nat1 = str(player.get('nationality', '')).lower()
	nat2 = str(player.get('second_nationality', '')).lower()
	
	# nationality check
	if nat1 == 'israel' or nat2 == 'israel':
		return 100.0
	
	score_surname = 0
	score_first_name = 0
	score_city = 0
	
	name_parts = str(player.get('name', '')).lower().split()
	city = str(player.get('birth_city', '')).lower()
	
	# last name check
	for part in name_parts:
		if part in indicators['surnames_high_prob']:
			score_surname = 100
			break
		elif part in indicators['surnames_med_prob']:
			score_surname = 50
	
	# first name check
	for part in name_parts:
		if part in indicators['first_names_biblical']:
			score_first_name = 100
			break
	
	# birth city check
	if city in indicators['jewish_hubs_cities']:
		score_city = 100
	
	# weighted average
	WEIGHT_SURNAME = 0.50
	WEIGHT_FIRST_NAME = 0.25
	WEIGHT_CITY = 0.25
	
	final_probability = (score_surname * WEIGHT_SURNAME) + \
	                    (score_first_name * WEIGHT_FIRST_NAME) + \
	                    (score_city * WEIGHT_CITY)
	
	return round(final_probability, 2)


def process_players(raw_players):
	indicators = load_indicators()
	filtered_players = []
	
	for player in raw_players:
		probability = calculate_jewish_probability(player, indicators)
		
		if probability > 0:
			player['jewish_probability'] = probability
			filtered_players.append(player)
	
	return filtered_players
