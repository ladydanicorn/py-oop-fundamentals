# Task 1

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

car1 = Vehicle("123456", "Sedan", "Kim")
car1.update_owner("Kim")

print("Updated owner:", car1.owner)

# Task 2
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count

event1 = Event("Musical", "04/01/2025")

event1.add_participant()
event1.add_participant()       

print("Current Participant Count:", event1.get_participant_count())
