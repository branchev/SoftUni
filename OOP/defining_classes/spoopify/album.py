# from project.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = [s for s in args]
        self.published = False

    def add_song(self, song):
        if not self.published:
            if song not in self.songs and not song.single:
                self.songs.append(song)
                return f"Song {song.name} has been added to the album {self.name}."
            elif song.single:
                return f"Cannot add {song.name}. It's a single"
            return "Song is already in the album."
        return "Cannot add songs. Album is published."

    def remove_song(self, song_name: str):
        if not self.published:
            try:
                song_to_remove = [song_class for song_class in self.songs if song_class.name == song_name][0]
                self.songs.remove(song_to_remove)
                return f"Removed song {song_name} from album {self.name}."
            except IndexError:
                return "Song is not in the album."
        return "Cannot remove songs. Album published."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        output = f"Album {self.name}\n"
        for song in self.songs:
            output += f"== {song.get_info()}\n"
        return output

#
# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
