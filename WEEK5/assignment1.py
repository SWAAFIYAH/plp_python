class Animal:
   def __init__(self, name, gender, color,):
    self.name = name
    self.gender = gender
    self.color = color
    
   def eat(self):
        print(f"{self.name}s eat food")
class Dog(Animal):
   def eat(self):
      print("dog eats meat")
class Goat(Animal):
   def eat(self):
      print("goats eat grass")
class Cat(Animal):
   def eat(self):
      print("cats eat meat")

dog = Dog("mimo", "she-dog","black")
goat = Goat("goat", "he-goat", "black")
cat = Cat("cuty", "she-cat", "white")
cat.eat()
dog.eat()
goat.eat()
      
   
        


      
      