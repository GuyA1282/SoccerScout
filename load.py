from models import Player, Session


def save_players_to_db(filtered_players_list):
	session = Session()
	
	for p_data in filtered_players_list:
		# is the player in the DB?
		existing_player = session.query(Player).filter_by(name=p_data['name']).first()
		
		if existing_player:
			existing_player.jewish_probability = p_data['jewish_probability']
			existing_player.birth_city = p_data['birth_city']
		else:
			new_player = Player(
				name=p_data['name'],
				nationality=p_data['nationality'],
				birth_city=p_data['birth_city'],
				jewish_probability=p_data['jewish_probability']
			)
			session.add(new_player)
	
	# close the connection
	session.commit()
	session.close()
	
	print(f"Successfully processed {len(filtered_players_list)} players.")
