class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, names):
        if species == "mammal":
            self.mammals.append(names)
        if species == "fish":
            self.fishes.append(names)
        if species == "bird":
            self.birds.append(names)

        Zoo.__animals += 1

    def get_info(self,species):
        total_animals = Zoo.__animals

        if species == "mammal":
            print(f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {total_animals}")
        if species == "fish":
            print(f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {total_animals}")
        if species == "bird":
            print(f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {total_animals}")


name = input()
number = int(input())

Zoo_var = Zoo(name)

for each in range(number):  #range(1, number + 1):
    command_list = input().split(" ")
    Zoo_var.add_animal(command_list[0],command_list[1])

option = input()

Zoo_var.get_info(option)