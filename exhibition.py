from artwork import Artwork

# making Exhibition class (inherits Artwork class also) 
class Exhibition(Artwork):
    def __init__(self, title, artist, date_of_creation, historical_significance, location, start_date, end_date, exhibition_type):
        super().__init__(title, artist, date_of_creation, historical_significance, location)
        self.start_date = start_date
        self.end_date = end_date
        self.exhibition_type = exhibition_type

    def display_exhibition_info(self):
        base_info = super().display_info()
        extra_info = (f", Start Date: {self.start_date}, End Date: {self.end_date}, "
                      f"Exhibition Type: {self.exhibition_type}")
        return base_info + extra_info
