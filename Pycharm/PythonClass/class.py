class student:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def display(self):
        print(self.name, self.age)


s1 = student('john', 56)
s1.display()

