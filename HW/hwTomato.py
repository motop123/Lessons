class Car():
    """Class of create car"""

    def __init__(self, make, model, year):
        """Attribute initialization"""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def description_name(self):
        """Discription car"""

        desc = str(self.year) + " " + self.make + " " + self.model
        return desc.title()
    def read_odometer(self):
        """Output car"""
        print(f'Odometer car {self.odometer_reading} kilomiters')
my_car = Car('Audi', 'a4', 2017)

print(my_car.description_name())
my_car.odometer_reading = 30
my_car.read_odometer()
