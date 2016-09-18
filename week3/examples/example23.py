# Пример работы с аттрибутами класса и инстанса


class Song(object):
    tags = []

    def __init__(self, artist, song):
        self.artist = artist
        self.song = song
        self.tags = []

    def add_tags(self, *args):
        self.tags.extend(args)

song1 = Song("John Mayer", "Gravity")
song1.add_tags("Blues", "Acoustic")

song2 = Song("Johny Cash", "The Man Comes Around")
song2.add_tags("Country")

print(song2.tags)  # Ожидаем на выходе только "Country"

print(print(Song.__dict__))