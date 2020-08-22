import time
class Animals():
    def bird(self, name, weight, colour):    
        self.name = name
        self.weight = weight
        self.colour = colour
    def birdy(self):
        print(f"\nFollowing are the details of your bird: \nName\t:\t{self.name} \nWeight\t:\t{self.weight} \nColour\t:\t{self.colour}")

pet = Animals()
pet.bird(input("Enter your bird name\n"), input("Enter the weight of your bird\n"), input("Enter the colour of your bird\n"))
pet.birdy()
time.sleep(10)