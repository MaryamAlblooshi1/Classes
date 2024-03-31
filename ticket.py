# making Ticket class
class Ticket:
    def __init__(self, ticket_id, price, event_date, location, visitor):
        self.ticket_id = ticket_id
        self.price = price
        self.event_date = event_date
        self.location = location
        self.visitor = visitor

    def calculate_price(self):
        if self.visitor.visitor_type in ["child", "teacher/student", "senior"]:
            return 0
        elif self.visitor.visitor_type == "group":
            return self.price * 0.5
        else:
            return self.price * 1.05 

    def display_ticket_info(self):
        final_price = self.calculate_price()
        return (f"Ticket ID: {self.ticket_id}, Date: {self.event_date}, Location: {self.location}, "
                f"Visitor: {self.visitor.name}, Final Price: {final_price} AED")
