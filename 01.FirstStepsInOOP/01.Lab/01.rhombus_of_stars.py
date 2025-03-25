class RhombusOfStars:
    def __init__(self, size):
        self.size = size

    def print_row(self, count):
        print(" " * (self.size - count) + "* " * count)

    def print_rhombus(self):
        for i in range(1, self.size + 1):
            self.print_row(i)

        for i in range(self.size - 1, 0, -1):
            self.print_row(i)


n = int(input())
rhombus = RhombusOfStars(n)
rhombus.print_rhombus()
