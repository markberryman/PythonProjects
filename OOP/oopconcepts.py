class Classroom:

    def __init__(self):
        # convention to use leading underscore to denote it's only
        # supposed to be used within the class; but this is not
        # enforced
        self._people = []

    def add_person(self, person):
        self._people.append(person)

    def remove_person(self, person):
        self._people.remove(person)

    def greet(self):
        for person in self._people:
            person.say_hello()

class Person:

    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        print("Hello,", self.name)

room = Classroom()
room.add_person(Person("Mark"))
room.add_person(Person("Bill"))

room.greet()
