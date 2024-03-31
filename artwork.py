# making Artwork class 
class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location

    def display_info(self):
        info = (f"Title: {self.title}, Artist: {self.artist}, "
                f"Date of Creation: {self.date_of_creation}, "
                f"Historical Significance: {self.historical_significance}, "
                f"Location: {self.location}")
        return info
