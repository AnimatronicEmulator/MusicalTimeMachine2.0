import requests
from bs4 import BeautifulSoup


class Souper:
    def __init__(self, date):
        self.time_machine_date = date
        self.wayback_url = "https://web.archive.org/web/20190602215844/https://www.billboard.com/charts/hot-100/"
        self.response = requests.get(url=f"{self.wayback_url}{self.time_machine_date}")
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.hot_100_tracks = self.get_tracks()
        self.hot_100_artists = self.get_artists()

    def get_tracks(self):
        song_titles_list = [title.getText().strip() for title in
                            self.soup.find_all(name="span", class_="chart-list-item__title-text")]
        return song_titles_list

    def get_artists(self):
        artists_list = [artist.getText().strip() for artist in
                        self.soup.find_all(name="div", class_="chart-list-item__artist")]
        return artists_list

