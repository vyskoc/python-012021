class Employee:
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}."
    def __init__(self, name, position, salary, children):
        self.name = name
        self.position = position
        self.salary = salary
        self.children = children
    def get_net_salary(self):
        dan = 0.15 * self.salary - 1500 * self.children
        cista = self.salary - dan
        return cista
    def get_tax(self):
        dan = 0.15 * self.salary - 1500 * self.children
        return dan
    def cistaMzda(self):
        cistaMzda = self.salary - self.get_tax()
        return cistaMzda
franta = Employee("FrantišekV", "skladník", 28000, 4)
print(franta.get_net_salary())
print(franta.cistaMzda())