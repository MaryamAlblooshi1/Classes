### in this file we will write test cases to check our system

from museum import Museum
from artwork import Artwork
from exhibition import Exhibition
from visitor import Visitor
from ticket import Ticket
from event import Event

# museum instance
louvre_museum = Museum()

# adding new artwork (https://www.louvreabudhabi.ae/en/explore/highlights-of-the-collection/astrolabe)
mona_lisa = Artwork("Astrolabe", 
                     "Muhammad ibn Ahmad Al-Battûtî", 
                       "1726-1727",
                         "A flat projection of the night sky, an astrolabe was used to help calculate the positions of the stars and to determine the exact time during the day. Mentioned by several ancient Greek authors, this measuring and navigational instrument was used up to the 18th century, when it was replaced by more sophisticated optical instruments. Combining the scientific knowledge of the East and West, this finely engraved astrolabe stands out due to its size, exceptional for this type of artefact.",
                           "Permanent Gallery")
print(louvre_museum.add_artwork(mona_lisa))

# organizing a new exhibition (https://www.louvreabudhabi.ae/en/explore/cartier)
modern_design_exhibition = Exhibition("Cartier, Islamic Inspiration and Modern Design",
                                  "Various",
                                    "2024",
                                      "Featuring over 400 works including jewellery and precious objects, masterpieces of Islamic art, drawings, textiles and photographs, the exhibition showcases the influences of the Islamic arts on Cartier's designs, from the beginning of the 20th century to the present day.",
                                        "Exhibition Hall", "16 November 2023", "24 March 2024", "temporary")
print(louvre_museum.organize_exhibition(modern_design_exhibition))

# purchasing tickets for maryam
visitor_maryam = Visitor("Maryam", 20, "teacher/student")
maryam_ticket = Ticket("T-001", 63, "2024-05-15", "Exhibition Hall", visitor_maryam)
print(louvre_museum.purchase_ticket(maryam_ticket).display_ticket_info())


# now making ticket for child visitor
visitor_ifrah = Visitor("Ifrah", 14, "child") 
ifrah_ticket = Ticket("T-002", 63, "2024-12-25", "Outdoor Space", visitor_ifrah)
print(louvre_museum.purchase_ticket(ifrah_ticket).display_ticket_info())


# now making ticket for senior visitor 
visitor_bushra = Visitor("Bushra", 65, "senior") 
bushra_ticket = Ticket("T-003", 63, "2024-12-25", "Outdoor Space", visitor_bushra)
print(louvre_museum.purchase_ticket(bushra_ticket).display_ticket_info())

# now making ticket for group purshase
visitor_group = Visitor("Group Purchase", 0, "group")
group_ticket = Ticket("T-004", 63, "2024-12-25", "Outdoor Space", visitor_group)
print(louvre_museum.purchase_ticket(group_ticket).display_ticket_info())

# purchasing tickets for laiba
visitor_laiba = Visitor("Laiba", 25, "General")
laiba_ticket = Ticket("T-005", 63, "2024-05-15", "Exhibition Hall", visitor_laiba)
print(louvre_museum.purchase_ticket(laiba_ticket).display_ticket_info())

# printing payment receipts only
print(louvre_museum.display_receipt("T-001"))
print(louvre_museum.display_receipt("T-002"))
print(louvre_museum.display_receipt("T-003"))
print(louvre_museum.display_receipt("T-004"))
print(louvre_museum.display_receipt("T-005"))