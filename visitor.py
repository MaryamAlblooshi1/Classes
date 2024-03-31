# making visitor class
class Visitor:
    def __init__(self, name, age, visitor_type):
        self.name = name
        self.age = age
        self.visitor_type = visitor_type

    def register_visit(self):
        return f"{self.name} registered as a {self.visitor_type} visitor."
