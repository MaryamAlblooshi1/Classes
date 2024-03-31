# making Event class 
class Event:
    def __init__(self, event_name, event_date, location, ticket_price):
        self.event_name = event_name
        self.event_date = event_date
        self.location = location
        self.ticket_price = ticket_price

    def display_event_info(self):
        return (f"Event Name: {self.event_name}, Date: {self.event_date}, "
                f"Location: {self.location}, Ticket Price: {self.ticket_price} AED")
