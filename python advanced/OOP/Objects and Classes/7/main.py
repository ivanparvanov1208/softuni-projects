from project.album import Album
from project.song import Song
from project.band import Band

band = Band("Death")
album = Album("The Sound of Perseverance")
print(band.remove_album("The Sound of Perseverance"))
