class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people_dict: list) -> list:
    person_list = []
    for person in people_dict:
        new_person = Person(person['name'], person['age'])
        person_list.append(new_person)

    for person in people_dict:
        person_name = person["name"]
        current_person = Person.people[person_name]

        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            current_person.wife = Person.people[wife_name]

        if "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            current_person.husband = Person.people[husband_name]

    return person_list




