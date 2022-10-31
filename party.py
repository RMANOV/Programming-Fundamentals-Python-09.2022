

class Party:
    people = []

    def __init__(self):
        self.people = []

    def people_add(self,person):
        while person == "End":
            break
        else:
            self.people.append(person)
            return self.people

    def print_people(self):
        return f"Going: {', '.join(self.people)}"

    def __repr__(self):
        return f"Total people: {len(sorted(self.people))}"

party = Party("Peter", "George")
print(party.people_add("End"))
print(party.print_people())
print(party)


# Output:
# ['Peter', 'George']
# Going: Peter, George
# Total people: 2
#  [Program finished]

# Path: party.py