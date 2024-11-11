# encapsulation
class shop:
    def __init__(self,balance):
        self.__balance=balance #Private method
    def amount(self,amount):
        if amount>=0:
            self.__balance+=amount
    def get(self,balance):
        return self.__balance
my_obj=shop(30)
my_obj.amount(20)
my_obj.amount(30)
my_obj.amount(40)
my_obj.amount(50)
print(my_obj.get(30))
#Inheritance
class Animal:
    def eat(self):
        return "Dog is eating"
class Dog(Animal):
    def bark(self):
        return "Dog is Barking"
my_obj=Dog()
print(my_obj.eat())
print(my_obj.bark())
#Multiple inheritance
print("Mutiple Inheritance")
class electronics:
    def is_on(self):
        print("Yes it is on!")
class diagonisis:
    def is_working(self):
        print("Yes it is working")
class appliances(electronics,diagonisis):
    def cool(self):
        print("The job is cooling")
my_obj3=appliances()
my_obj3.is_working()
my_obj3.is_on()
my_obj3.cool()
#MultiLevel Inheritance
#Inherits the property
print("Multilevel inheritance")
class vehicle:
    def start(self):
        print("This Vehicle Needs to be Started using button")
class car(vehicle):
    def brand(self):
        print("The brand is Buggati")
class feature(car):
    def turbo_boost(self):
        print("Turbo_boost is Activated")
my_obj4=feature()
my_obj4.brand()
my_obj4.start()
my_obj4.turbo_boost()
#Hierarichal Inheritance
class Animal:
    def breathe(self):
        print("The animal is Breathing")
class dog(Animal):
    def bark(self):
        print("The dog is barking")
class cat(Animal):
    def meow(self):
        print("The cat is meowing")
doggy=dog()
catty=cat()
doggy.bark()
catty.meow()
doggy.breathe()
catty.breathe()
#Hybrid inheritance is the multiple inheritance
class Car:
    def start(self):
        print("Started the Car")
class Drive(Car):
    def drive(self):
        print("Driving the car")
class speed:
    def mx_spd(self):
        print("It's Maximum speed is about 450KMPH")
class brand(Drive,speed):
    def electric(self):
        print("This is an electric car")
car=brand()
car.mx_spd()
car.drive()
car.start
















