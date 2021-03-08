# from project.keeper import Keeper
# from project.caretaker import Caretaker
# from project.cheetah import Cheetah
# from project.lion import Lion
# from project.tiger import Tiger
# from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if len(self.animals) < self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        searched_worker = [w for w in self.workers if w.name == worker_name]
        if searched_worker:
            self.workers.remove(searched_worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        wage_fund = sum([w.salary for w in self.workers])
        if self.__budget >= wage_fund:
            self.__budget -= wage_fund
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needs_of_animals_fund = sum([a.get_needs() for a in self.animals])
        if self.__budget >= needs_of_animals_fund:
            self.__budget -= needs_of_animals_fund
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        output = f"You have {total_animals_count} animals\n"

        output += f"----- {len(lions)} Lions:\n"

        for lion in lions:
            output += f"{lion}\n"

        output += f"----- {len(tigers)} Tigers:\n"

        for tiger in tigers:
            output += f"{tiger}\n"

        output += f"----- {len(cheetahs)} Cheetahs:\n"

        for cheetah in cheetahs:
            output += f"{cheetah}\n"

        return output.rstrip()

    def workers_status(self):
        total_workers_count = len(self.workers)
        keepers = [a for a in self.workers if a.__class__.__name__ == "Keeper"]
        caretakers = [a for a in self.workers if a.__class__.__name__ == "Caretaker"]
        vets = [a for a in self.workers if a.__class__.__name__ == "Vet"]

        output = f"You have {total_workers_count} workers\n"

        output += f"----- {len(keepers)} Keepers:\n"

        for keeper in keepers:
            output += f"{keeper}\n"

        output += f"----- {len(caretakers)} Caretakers:\n"

        for caretaker in caretakers:
            output += f"{caretaker}\n"

        output += f"----- {len(vets)} Vets:\n"

        for vet in vets:
            output += f"{vet}\n"

        return output.rstrip()

# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
