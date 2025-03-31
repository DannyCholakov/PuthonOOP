from math import floor

class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(floor(float_value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
                      'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                      'D': 500, 'CM': 900, 'M': 1000}

        num, i = 0, 0
        while i < len(value):
            if i+1 < len(value) and value[i:i+2] in roman_dict:
                num += roman_dict[value[i:i+2]]
                i += 2
            else:
                num += roman_dict[value[i]]
                i += 1
        return cls(num)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str) and value.isdigit():
            return cls(int(value))
        return "wrong type"
