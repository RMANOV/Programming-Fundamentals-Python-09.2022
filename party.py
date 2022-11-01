

class Person:

        def __init__(self, name):
            self.name = name

class Party:

        def __init__(self):
            self.people = []

        def invite(self, person):
            self.people.append(person)

        def name_of_invited(self):
            return [person.name for person in self.people]

        def number_of_guests(self):
            return len(self.people)

Party = Party()
 
while True:

    command = input()

    if command == 'End':
        break

    name = command
    person = Person(name)
    Party.invite(person)


print(f'Going: {", ".join(Party.name_of_invited())}')
print(f'Total: {Party.number_of_guests()}')
