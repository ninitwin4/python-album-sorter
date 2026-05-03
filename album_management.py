# Design a class called Album
class Album:

    # Constructor for three instance variables
    def __init__(self, album_name, number_of_songs, album_artist):
        # Initialize instance variables
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    # String representation of Album object
    # Returns format: (album name, album artist, number of songs)
    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"
    
# Create Albums1 & add five album objects
albums1 = [
    Album("MoonMusic", 10, "Coldplay"),
    Album("Lemonade", 13, "Beyonce"),
    Album("Shawn", 12, "Shawn Mendes"),
    Album("GNX", 12, "Kendrick Lamar"),
    Album("30", 12, "Adele")
]

# Print out albums1
for album in albums1:
    print(album)

# Sorting albums1 by number of songs using the key parameter
albums1.sort(key=lambda album: album.number_of_songs)
# Print the sorted albums1
for album in albums1:
    print(album)

# Swap the element at index 0 AND index 1 at the same time,
# index 0 gets what was at index 1 and index 1 gets
# what was at index 0
albums1[0], albums1[1] = albums1[1], albums1[0]
# Print albums1 after swap
print("\n--- albums1 (after swapping index 0 and index 1) ---")
for album in albums1:
    print(album)

# Create Albums2 with five album objects
albums2 = [
    Album("Invasion of Privacy", 13, "Cardi B"),
    Album("For All The Dogs", 23, "Drake"),
    Album("SWAG II", 44, "Justin Bieber"),
    Album("The Life of a Showgirl", 12, "Taylor Swift"),
    Album("The Art of Loving", 12, "Olivia Dean")
]

# Print out albums2
print("\n--- albums2 ---")
for album in albums2:
    print(album)

# Copy all albums from albums1 into albums2, using extend()
albums2.extend(albums1)
# Add two more Album objects to albums2
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!...I Did It Again", 16, "Britney Spears"))

# Sort albums2 alphabetically by album_name & print the sorted albums2
albums2.sort(key=lambda album: album.album_name)
print("\n--- albums2 (sorted alphabetically by album name) ---")
for album in albums2:
    print(album)

# Search for Dark Side of the Moon in albums2 and print its index 
print("\n--- Search Result ---")
for index, album in enumerate(albums2):
    if album.album_name == "Dark Side of the Moon":
        print(f"{album.album_name} found at index {index}")
