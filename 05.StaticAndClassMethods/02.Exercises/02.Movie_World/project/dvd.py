class DVD:
    MONTHS = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        day, month, year = map(int, date.split('.'))
        month_name = cls.MONTHS[month - 1]
        return cls(name, id, year, month_name, age_restriction)

    def __repr__(self):
        status = "rented" if self.is_rented else "not rented"
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "
                f"has age restriction {self.age_restriction}. Status: {status}")
