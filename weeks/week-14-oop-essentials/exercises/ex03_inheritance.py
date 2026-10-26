"""Exercise 03: one clear basic inheritance example."""


class Animal:
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"


dog = Dog("Milo")
print(dog.speak())
print(isinstance(dog, Animal))  # True

# Dog is an Animal: mọi Dog đều là một loại Animal.
