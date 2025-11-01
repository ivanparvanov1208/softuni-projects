from .song import Song

class Album:
    def __init__(self, name, *songs: Song):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return f"Cannot add songs. Album is published."
        elif song in self.songs:
            return f"Song is already in the album."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song_removed = False
        for i in range(len(self.songs)):
            if self.songs[i].name == song_name:
                if not self.published:
                    self.songs.pop(i)
                    song_removed = True
                else:
                    return f"Cannot remove songs. Album is published."
                break

        if song_removed:
            return f"Removed song {song_name} from album {self.name}."
        else:
            return "Song is not in the album."



    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        songs = "\n".join("== " + s.get_info() for s in self.songs)
        return f"Album {self.name}\n{songs}\n"