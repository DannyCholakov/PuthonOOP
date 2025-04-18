class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type  # Setter validates
        self.baking_technique = baking_technique  # Setter validates
        self.weight = weight  # Setter validates

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, value: str):
        if value == "":
            raise ValueError("The flour type cannot be an empty string")
        self.__flour_type = value

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, value: str):
        if value == "":
            raise ValueError("The baking technique cannot be an empty string")
        self.__baking_technique = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = value
