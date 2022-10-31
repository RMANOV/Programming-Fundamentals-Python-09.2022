

class Party:
    people = []

    def __init__(self, *args):
        self.people = list(args)

    def people_add(self,person):
        while person == "End":
            break
        else:
            self.people.append(person)
            return self.people

    def print_people(self):
        return f"Going: {', '.join(self.people)}"

    def __repr__(self):
        return f"Party({self.people})"

party = Party("Peter", "George")
print(party.people_add("End"))
print(party.print_people())
print(party)


    
            