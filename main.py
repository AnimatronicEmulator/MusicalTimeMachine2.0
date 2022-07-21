from souper import Souper
from spotifyer import Spotifyer

specified_date = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")
souper = Souper(specified_date)
spotifyer = Spotifyer()

song_uris = []
for x in range(100):
    song_uris.append(spotifyer.uri_generator(song_title=souper.hot_100_tracks[x],
                                             artist_name=souper.hot_100_artists[x]))

while "Sorry, nope" in song_uris:
    song_uris.remove("Sorry, nope")

playlist_link = spotifyer.playlist_maker(name_of_playlist=f"{specified_date} Billboard Hot 100",
                                         list_of_tracks=song_uris)
print(playlist_link)
