from artwork import Artwork
from exhibition import Exhibition
from event import Event
from visitor import Visitor
from ticket import Ticket

class Museum:
    def __init__(self):
        self.artworks = []
        self.exhibitions = []
        self.events = []
        self.visitors = []
        self.tickets = []

    def add_artwork(self, artwork):
        if isinstance(artwork, Artwork):
            self.artworks.append(artwork)
            return f"Artwork '{artwork.title}' added successfully."
        return "Failed to add artwork."

    def organize_exhibition(self, exhibition):
        if isinstance(exhibition, Exhibition):
            self.exhibitions.append(exhibition)
            return f"Exhibition '{exhibition.title}' organized successfully."
        return "Failed to organize exhibition."

    def organize_event(self, event):
        if isinstance(event, Event):
            self.events.append(event)
            return f"Event '{event.event_name}' organized successfully."
        return "Failed to organize event."

    def purchase_ticket(self, ticket):
        if isinstance(ticket, Ticket):
            self.tickets.append(ticket)
            return ticket
        
    def display_receipt(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket.display_ticket_info()
        return "Ticket not found."

