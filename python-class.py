class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        return f"Rectangle with width {self.width} and height {self.height} has an area of {self.area()} and a perimeter of {self.perimeter()}."

rect = Rectangle(10, 20)

print(rect.area())

perim = Rectangle(30, 40)  #Output 200
print(perim.perimeter()) #Output 140

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 4)

print(dog1.description())  # Output: Buddy is 3 years old
print(dog2.speak("Woof"))  # Output: Lucy says Woof

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0
counter = Counter()
print(counter.count)  # Output: 0

counter.increment()
print(counter.count)  # Output: 1

counter.reset()
print(counter.count)  # Output: 0
