class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} makes a sound: {self.sound}")

class Dog(Animal):
    def __init__(self, species, sound, breed):
        super().__init__(species, sound)
        self.breed = breed

    def make_sound(self):
        super().make_sound()
        print("Woof!")


class Cat(Animal):
    def __init__(self, species, sound):
        super().__init__(species, sound)

    def make_sound(self):
        print(f"The {self.species} makes a sound: {self.sound}")


class Pet:
    def is_pet(self):
        print("It's a pet.")

dog = Dog("Dog", "Bark", "Golden Retriever")
dog.make_sound()
print("Breed:", dog.breed)

cat = Cat("Cat", "Meow")
cat.make_sound()

class PetDog(Dog, Pet):
    pass

pet_dog = PetDog("Dog", "Bark", "Poodle")
pet_dog.make_sound()
pet_dog.is_pet()
