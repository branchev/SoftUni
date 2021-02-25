# from project.album import Album
# from project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        try:
            searched_album = [album for album in self.albums if album.name == album_name][0]
            if not searched_album.published:
                self.albums.remove(searched_album)
                return f"Album {album_name} has been removed."
            return f"Album has been published. It cannot be removed."

        except IndexError:
            return f"Album {album_name} is not found."

    def details(self):
        output = f"Band {self.name}\n"
        for album_class in self.albums:
            output += f"{album_class.details()}\n"
        return output

#
# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
