class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __str__(self):
        members = ', '.join(str(p) for p in self.people)
        return f"Group {self.name} with members {members}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"

    def __iter__(self):
        for i, person in enumerate(self.people):
            yield f"Person {i}: {person}"
