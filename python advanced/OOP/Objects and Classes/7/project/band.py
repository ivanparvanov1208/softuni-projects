from .album import Album

class Band:
    def __init__(self, name):
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        album_removed = False
        for i in range(len(self.albums)):
            if self.albums[i].name == album_name:
                if not self.albums[i].published:
                    self.albums.pop(i)
                    album_removed = True
                else:
                    return "Album has been published. It cannot be removed."
                break

        if album_removed:
            return f"Album {album_name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        albums = "\n".join(a.details() for a in self.albums)
        return f"Band {self.name}\n{albums}\n"