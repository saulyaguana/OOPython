class Student:
    def __init__(self, name, email_address, current_grade, school, age):
        self.name = name
        self.email_address = email_address
        self.current_grade = current_grade
        self.school = school
        self.age = age
        
class Player:
    def __init__(self, name, points, health, location):
        self.name = name
        self.points = ponts
        self.health = health
        self.location = location
        
    def win(self, reach_points):
        if self.points >= reach_points:
            return True
        return False
    
    def lose(self, reach_points):
        if self.points < reach_points or self.health <= 0:
            return True
        return False
    
    def find_player(self, location):
        if self.location["x"] == location["x"] and self.location["y"] == location["y"]:
            return True
        return False
    
class Person:
    def __init__(self, name, address, phone_number, birthday):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.birthday = birthday
        
if __name__ == "__main__":
    player1 = Player("Leon-main", 45, 22, {"x": 129, "y": 443.8})
