# procedual-->functional-->oop
# map with the real word scenarios, we started using object in code.this is called object orianted programming.
# object->class
# self==s1 (self parameter point to the object at which location.)
# s1=student()(s1 is creating object also called instance)
# shradhha khapra
# =============================================================
# proecudual programming 
# for example we have a task to make a sum of two number 
a=1
b=2
if a<=b:
    print('number is less then b and the number is ', a) 
else :
    print(' number is grater then a and the number is', b)

# =====================================================
# functional  programming  this is used for grouping the code to make less redundency in the code basically not to repete the code when ever we need the code call the function and execute the same code 
def fun(a, b):# function defination
    if (a<=b):
        print('number is less then b and the number is ', a) 
    else :
        print(' number is grater then a and the number is', b)

fun(6,3) #function  call 

# ====================================================================
# object oriantation programming 
# to map the real world scenarios , we started using objects in code.
# this is called object oriented programming
# class is the blueprint for creating  object
# creating class
class Student:
    name='abhishek'

# creating object (instance)
s1=Student()
print(s1.name)
class Car:
    colour="black"
    brand="mercedes"
cr1=Car()
print(cr1.colour)
print(cr1.brand)

# ===================================================================
# __init__function
# constructor (this is the function which is automatically called when the object is created , all classes have a function called __init__(), which is always executed when the object is initated .)
#creating class
class Student :
    def __init__(self, fullname):
        self.fullname=fullname
#creating the object 
s1=Student('abhisek :)')
print(s1.fullname)
# the self parameter is the default parameter which is use to point the  attrtibutes that is belongs to that object
# or we can say the self parameter is the reference of the current object (instance) 
# s1==self
# there are two types of constructoir 1)default constructor and 2) parameteriased constructor

# ===============================================================
# classes and instance of attributes
# class.attr(the attributs which are same in the each object we define in the class it self so that the attribut can access to all the object)
# obj.attr(the attributes which are different for each object we define in the particular object)
# object attributs precidence>class attributs precidence
class Student:
    collage_name='ABIT' #thios is class attribute
    name='annonymous'
    def __init__(self, name, mark):
        self.name=name #this is object attribute
        self.mark=mark
        print("adding new information in database...")
    def function_name(self):
    #function_body
         print('this is a method')

s1 = Student('ishani',92)
print(s1.name)
print(s1.collage_name)
print(s1.mark)
s1.function_name()

# ===========================================================
# method(methods are  function that belongs to objects)
# class= attributs + method
class Student:
    collage_name='ABIT' #thios is class attribute
    name='annonymous'
    def __init__(self, name, mark):
        self.name=name #this is object attribute
        self.mark=mark
        print("adding new information in database...")
    def function_name(self):
    #function_body
         print('this is a method')

s1 = Student('ishani',92)
print(s1.name)
print(s1.collage_name)
print(s1.mark)
s1.function_name()
# ===================================================================
"""practice --> create student class that takes name & marks of 3 subject as arguments in constructor .
then create a method to print the average."""
class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def avg(self):
        self.average=sum(self.marks)/len(self.marks)
        return f'the average of the subject is {self.average}'
s1= Student('ishani',[92,97,99])
print(s1.name)
print(s1.marks)
print(s1.avg())
# ===============================================================
# 
# static method(all the time we don't neeed to define the self so that we declare as static method)
# @staticmethod is a decorator which takes the input as function and gives the output as function which is change the behaviour of an normal method  
class Student :
    @staticmethod #decorator
    def collage():
        print("ABC collage")
s2= Student()
s2.collage()
# ===============================================================
# important
# 4 pillor of object oriented programming which are --> inharitance, abstraction, polimorphism, encapsulation
# abstruction-->hiding the impelementation details of a class and only showing the essential features to the user .
# suppose the car has to start then will show the status if function call it will start but will not show what is the changes inside the class sob that it is starting the car
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True # this things are not showing outside the class , hidden from the user
        print("car started.....")

s1=Car()# encaptulation
s1.start()
# Encaptulation-->Wrapping data and function into a single unit(object)
# =====================================================================
# practice
# create account class with 2 attributs -- balance and account no. create methods for debit, credit and printing the balance.
class Account:
    balance=0
    account_number=12345
    def debt(self,debt_amt):
        self.debt_amt=debt_amt
        self.balance=self.balance-debt_amt
        print("amount debited rs.  ",debt_amt)
        print("the total balance now ",self.balance)
    def crdt(self,crdt_amt):
        self.crdt_amt=crdt_amt
        self.balance=self.balance+crdt_amt
        print("amount credited rs.  ",crdt_amt)
        print("the total balance now ",self.balance)

a1=Account() 
a1.balance=2000
a1.debt(700) 
a1.crdt(300)   
# ===============================================================
# private attributes and method which are not accessable outside the class which can only be accessible inside th e class perpose of creating this function and attribute to secure data or for internal use only example the account method  can have many sensative data like account number and all so we want to use inside the class but shoud not be accessable outside the class that time we make the attribute or the function as private
# create account class with 2 attributs -- balance and account no. create methods for debit, credit and printing the balance.
class Account:
    def __init__(self):
        self.balance=0
        self.__account_number=12345 #giving __ before any attribute makes it a private attribute 
    def __debt(self,debt_amt): # giving __ before any function makes it as private method 
        self.debt_amt=debt_amt
        self.balance=self.balance-debt_amt
        print("amount debited rs.  ",debt_amt)
        print("the total balance now ",self.balance)
    def __crdt(self,crdt_amt):
        self.crdt_amt=crdt_amt
        self.balance=self.balance+crdt_amt
        print("amount credited rs.  ",crdt_amt)
        print("the total balance now ",self.balance)
    def run_debt(self):
         self.__debt(700)  
    def run_crdt(self):
        self.__crdt(300)   
    def act_no(self):
        print("the account number is",self.__account_number)
        

a1=Account() 
a1.balance=2000 
# a1.debt(700) # will throw an error
# a1.crdt(300)  # will throw an error
a1.run_debt()
a1.run_crdt()
a1.act_no() 
# ==================================================================
# inharitance(when one class (child class) inharit all the property of another class(parants class) is called as inharitance)
"""class Car:
    .....
class Toyota(Car):
    ....."""
class Car():
    def start(self):
        print("car started ......")
    def stop(self):
        print("car stopped .......")
class Model(Car):
    def __init__(self):
        print("Toyota,\t")
        print(self.start())
t1= Model()
# ============================================================
# inharitance type 
# single inharitance(parant class-->chaild class)
"""class Car:
    .....
class Toyota(Car):
    ....."""
# multi-level inharitance
"""class Car:
    .....
class Toyota(Car):
    .....
class fourtuner(Toyota):
    .....
    """
# multiple inharitance
"""class CarA:
    .....
    class CarB:
    .....
    class CarC(CarA,CarB):
    .....

    """
# ========================================================================
# super method
# super() method is used to access method of the parent class
# =======================================================================

# class method (a class method is bound to the class and receives the class  as an implicit first argument.note static method can't access or modify class state and generally for utility.)
class Student:
    @classmethod #decorator
    def collage(cls):
        pass
"""1)static method (@staticmethod)
   2)class method(cls)@classmethod
   3)instance method(self)"""
# ============================================================================
# property decorator(we use @property decorator on any method in class to use the method as a property)
# learn about @getter and @setter as well 
# =======================================================
# polimorphism
# 1)operator overloading
# 2)overriding
# operator and dunder function
