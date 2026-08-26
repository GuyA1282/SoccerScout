from extract import fetch_from_source
from transform import process_players
from load import save_players_to_db


def main():
	raw_data = fetch_from_source()
	
	filtered_data = process_players(raw_data)
	
	save_players_to_db(filtered_data)


if __name__ == "__main__":
	main()