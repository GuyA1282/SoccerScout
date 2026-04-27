import requests
from bs4 import BeautifulSoup


def scrape_sofascore():
	url = "https://www.sofascore.com"  # האתר שלוקחים ממנו את הנתונים
	headers = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
	}
	
	response = requests.get(url, headers=headers)
	
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'html.parser')
		# ננסה להדפיס את כל הכותרות (h1, h2) שיש בדף
		titles = soup.find_all(['h1', 'h2'])
		for t in titles:
			print(t.text.strip())
	else:
		print(f"Failed to connect. Status code: {response.status_code}")


if __name__ == "__main__":
	scrape_sofascore()
	