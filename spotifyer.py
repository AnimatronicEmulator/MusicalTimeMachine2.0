import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Spotifyer:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=config.spotify_client_id,
                client_secret=config.spotify_client_secret,
                redirect_uri="http://example.com",
                scope="playlist-modify-private",
                cache_path="token.txt",
                show_dialog=True,
            ))
        self.user_id = self.sp.current_user()['id']

    def uri_generator(self, song_title, artist_name):
        results = self.sp.search(q=f"track:{song_title}+artist:{artist_name}", type="track")

        try:
            song_uri = results["tracks"]["items"][0]["uri"]
        except IndexError:
            song_uri = "Sorry, nope"
            return song_uri
        else:
            for song in results["tracks"]["items"]:
                if song["name"] and song["artists"][0]["name"] in artist_name:
                    song_uri = song["uri"]
                    return song_uri

            return song_uri

    def playlist_maker(self, name_of_playlist, list_of_tracks):
        result = self.sp.user_playlist_create(user=self.user_id, name=name_of_playlist, public=False)
        self.sp.playlist_add_items(playlist_id=result["id"], items=list_of_tracks)
        return result["external_urls"]["spotify"]
