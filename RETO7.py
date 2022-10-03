
class Person: 
  def __init__(self, name: str, age: int, size: int, color: str):
    print("Person Created...")
    self.name = name
    self.age= age 
    self.size= size
    self.Hair_color = color

  def walk(self, distance: int):
    self. distance = distance
    print(f"Hi, my name is {self.name}, i walk {distance} m")

  def eat(self, food: str):
    self.food = food
    print(f"Hi, my name is {self.name} and i'm going to eat {self.food}")
  
  def speak(self, language: str):
    self.language = language
    print(f"Hi, my name is {self.name} and i speak {self.language}")


class Student(Person): 
    print("Student created...")
  
    def Study(self, subject: str):
        self.subject = subject
        print(f"Hi, my name is {self.name} and i'm studying {self.subject}")

class Teacher(Person): 
    print("Teacher created...")

    def Teach(self, subject: str):
        self.subject = subject
        print(f"Hi, my name is Sir.{self.name} and i'm teaching {self.subject}")


s1= Student("Carlos",13, 34, "red")

print(s1.walk(66))
print("----")
print(s1.eat(("cake")))
print("----")
print(s1.speak(("French")))
print("----")
print(s1.Study(("Chemistry")))

t1= Teacher("Ronald",45, 41, "black")

print(t1.walk(78))
print("----")
print(t1.eat(("Salad")))
print("----")
print(t1.speak(("German")))
print("----")
print(t1.Teach(("Math")))

