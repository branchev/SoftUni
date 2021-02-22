class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False
        self.water_amount = 0

    def status(self):
        if self.water_amount >= self.water_requirements:
            self.is_happy = True
            return f"{self.name} is happy"
        return f"{self.name} is not happy"

    def water(self, ml):
        self.water_amount = ml


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
