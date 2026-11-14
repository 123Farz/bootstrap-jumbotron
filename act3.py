class Siblings:

    species = "human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Rua = Siblings("Rua", 14)
Jo = Siblings("Jo", 13)

print("Rua is a {}" .format(Rua.species))
print("Jo is also a {}" .format(Jo.species))

print("{} is {} years old" .format(Rua.name, Rua.age))
print("{} is {} years old" .format(Jo.name, Jo.age))
print("Their age difference in years is:", (Rua.age - Jo.age))

