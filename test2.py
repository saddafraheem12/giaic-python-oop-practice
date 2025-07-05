# 1. Student Info
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def greet(self):
        print(f"Hello, I am {self.name} from grade {self.grade}.")

# 2. Car Details
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h.")

# 3. Book Details
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        print(f"Reading '{self.title}' by {self.author}")

# 4. Bank Account
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner}'s balance is ${self.balance}")

# 5. Light Bulb
class Bulb:
    def __init__(self, wattage):
        self.wattage = wattage

    def turn_on(self):
        print(f"The {self.wattage}W bulb is now on.")

# --- 2. Encapsulation ---

# 1. Bank Account Balance
class BalanceAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

# 2. Password Protection
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, pwd):
        return pwd == self.__password

# 3. Car Speed Control
class CarEncapsulated:
    def __init__(self):
        self.__speed = 0

    def accelerate(self):
        self.__speed += 10

    def get_speed(self):
        return self.__speed

# 4. ATM PIN
class ATM:
    def __init__(self, pin):
        self.__pin = pin

    def verify_pin(self, input_pin):
        return self.__pin == input_pin

# 5. Student Marks
class StudentMarks:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks

    def get_marks(self):
        return self.__marks

# --- 3. Polymorphism ---

class PaymentMethod:
    def pay(self):
        return "Processing payment"

class Cash(PaymentMethod):
    def pay(self):
        return "Paid using cash"

class Card(PaymentMethod):
    def pay(self):
        return "Paid using Debit/Credit Card"

class QR(PaymentMethod):
    def pay(self):
        return "Paid using QR code"

methods = [Cash(), Card(), QR()]
for m in methods:
    print(m.pay())
