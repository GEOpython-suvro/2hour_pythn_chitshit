"""String formatting"""
#way 1: (str.format)
a = 10
r = 3.14
area = a* r ** 2
print('The area of a circle with a radius {} is {:.2f}.'.format(r, area)) #The area of a circle with a radius 3.14 is 98.60.
#way 2: String Interpolation / f-Strings
print(f'{a} / {r} = {a / r:.2f}') #10 / 3.14 = 3.18

#Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P

#all string methods
str = 'thirty days of python'
print(str.capitalize()) #Thirty days of python
print(str.count('y')) #3
print(str.endswith('on')) #True
print(str.find('th')) #0
print(str.rfind('y')) #16
print(str.index('da')) #7
print(str.rindex('o')) #19
print(str.isalnum()) #False
print(str.isdecimal()) #False
print(str.isdigit()) #False
print(str.isnumeric()) #False
print(str.isidentifier()) #False ,checks if a string is a valid variable name
print(str.islower()) #True
print(str.isupper()) #False
print(str.strip('noth')) #irty days of py
print(str.replace('python', 'coding')) #thirty days of coding
print(str.split()) #['thirty', 'days', 'of', 'python']
s = '30, days, of, python'
print(s.split(', ')) #['30', 'days', 'of', 'python']
print(str.title()) #Thirty Days Of Python
print(str.swapcase()) #THIRTY DAYS OF PYTHON
print(str.startswith('thirty')) #True
txt = "H\te\tl\tl\to" 
print(txt)               #H       e       l       l       o
print(txt.expandtabs())  #H       e       l       l       o
print(txt.expandtabs(8)) #H       e       l       l       o
print(txt.expandtabs(10))#H         e         l         l         o

#string join with a list and converts list into a string
list = ['HTML', 'CSS', 'JavaScript', 'React']
print(' '.join(list))  #HTML CSS JavaScript React
print('#'.join(list))  #HTML#CSS#JavaScript#React

"""List"""
#Lists can have items of different data types
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]
last_index = len(lst) - 1

#unpacking list
countries = ['Germany', 'France','Finland','Estonia']
gr, *scandic, es = countries
print(gr) #Germany
print(scandic) #['France', 'Finland']
print(es) #Estonia

#reversing list
print(countries[::-1])  #['Estonia', 'Finland', 'France', 'Germany']

#modifying list
last_index = len(countries) - 1
countries[last_index] = 'India'
print(countries) #['Germany', 'France', 'Finland', 'India']

#Checking Items in a List
print('Finland' in countries) #True

#Adding Items to a List
countries.append('Brazil')
print(countries) #['Germany', 'France', 'Finland', 'India', 'Brazil']

#Inserting into a list: list.insert(index, item)
countries.insert(2, 'China')
print(countries) #['Germany', 'France', 'China', 'Finland', 'India', 'Brazil']

#removing item from list: list.remove(item)
countries.remove('India')
print(countries) #['Germany', 'France', 'China', 'Finland', 'Brazil']
#Removing Items Using Pop
countries.pop()  #remove last item
print(countries) #['Germany', 'France', 'China', 'Finland']

countries.pop(0) #remove indexed items
print(countries) #['France', 'China', 'Finland']

#removing using del
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[-3:-1] 
print(fruits) #['banana', 'orange', 'mango', 'lime']

#Copying a List
fruits_copy = fruits.copy()
print(fruits_copy) #['banana', 'orange', 'mango', 'lime']

#joining list
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
#joining list by extend method
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) #Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))    #3
print(ages.index(24))    #2

ages.reverse()
print(ages) #[24, 25, 24, 26, 25, 24, 19, 22]

ages.sort()
print(ages) #[19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #[26, 25, 25, 24, 24, 24, 22, 19]

"""Tuples(immutable): can't add, insert, remove methods  """
#Checking an Item in a Tuple.Tuple is immutable if we want to modify a tuple we should change it to a list.
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
#checking items in tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
#joining tuple
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
#It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
del tpl1

"""Sets"""
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item8') #single item adding
st.update(['item5','item6','item7']) #multiple item adding
st.remove('item2')
st.pop()  # removes a random item from the set
print(st) #{'item7', 'item4', 'item1', 'item8', 'item2', 'item5', 'item6', 'item3'}
st.clear() #{} or set()
del st 

"""Dictionaries"""
#Accessing an item by key name
person = {'first_name':'Asabeneh','age':250,'is_married':True,
'skills':['JavaScript', 'Python'],'address':{'street':'Space street','zipcode':'02210'}}
print(person.get('first_name')) #Asabeneh
#Adding Items to a Dictionary
person['key5'] = 'value5' 
person['skills'].append('HTML') 
print(person) #{'first_name': 'Asabeneh', 'age': 250, 'is_marred': True, 'skills': ['JavaScript', 'Python', 'HTML'], 'address': {'street': 'Space street', 'zipcode': '02210'}, 'key5': 'value5'}
person['first_name']='Shubro' #Modifying Items in a Dictionary
print('first_name' in person) # True
print('last_name' in person) # False
person.pop('address') #remove address key
person.popitem() #remove last key
del person['is_married'] #delete is_married key
#Dictionary to list of tuples:The items() method changes dictionary to a list of tuples.
print(person.items()) #dict_items([('first_name', 'Shubro'), ('age', 250), ('skills', ['JavaScript', 'Python', 'HTML'])])
print(person.clear()) # None
del person

"""Conditionals"""
a = 3
print('A is positive') if a > 0 else print('A is negative') #A is positive
#Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero') #A is zero
else:
    print('A is a negative number')
#We can avoid writing nested condition by using logical operator and.
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')  #A is zero
else:
    print('A is negative')

"""While loop:It is used to execute a block of statements repeatedly until a given condition is satisfied.
 When the condition becomes false, the lines of code after the loop will be continued to be executed."""
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count) # print from 0 to 5
#We use break when we like to get out of or stop the loop.
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break         #0 1 2
#With the continue statement we can skip the current iteration, and continue with the next:
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1 # 0 1 2 4 

"""For loop:Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary,
 a set, or a string)."""
 #For loop with list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)      # 0 1 2 3 4 5
#for loop with string
language = 'Python'
for letter in language:
    print(letter)      # P y t h o n
for i in range(len(language)):
    print(language[i]) # P y t h o n
#for loop with tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)   # 0 1 2 3 4 5
#for loop with dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)   # first_name  last_name  age  country  is_marred  skills address

for key, value in person.items():
    print(key, value) # first_name Asabeneh   last_name Yetayeh   age 250   country Finland .......................

#for loop with set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)  # Amazon Oracle Microsoft Facebook Google IBM Apple 

for number in range(11):
    print(number)   # prints 0 to 10, not including 11

#nested loop:we can write loop inside a loop
person = {'skills': ['JavaScript', 'React', 'Node', 'MongoDB','Python'],'address': {'street': 'Space street','zipcode': '02210'}}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)  #JavaScript  React   Node   MongoDB   Python
#If we want to execute some message when the loop ends, we use else.
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
#In python when statement is required (after semicolon), but we don't like to execute any code there,
# we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
for number in range(6):
    pass

"""Functions"""
#functions without parameter
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function
#Function can also return values, if a function does not have a return statement, the value of the function is None. 
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())  # 5
#If our function takes a parameter we should call our function with an argument
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
#A function may or may not have a parameter or parameters. A function may also have two or more parameters
def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81)) #Weight of an object in Newtons:  981.0 N
#If we pass the arguments with key and value, the order of the arguments does not matter.
def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # 5 None, None will show as we did not return function
#function returning a boolean
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False
#Function returning a list
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))  #[0, 2, 4, 6, 8, 10]
#Function with Default Parameters
#Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.
def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) #Weight of an object in Newtons:  981.0 N
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62))#Weight of an object in Newtons:  162.0 N
#Arbitrary Number of Arguments
#If we do not know the number of arguments we pass to our function, we can create a function which can take 
# arbitrary number of arguments by adding * before the parameter name.
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
#Default and Arbitrary Number of Parameters in Functions
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob')) #Team-1 Asabeneh Brook David Eyob None
#Function as a Parameter of Another Function
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27

"""List Comprehension"""
#For instance if you want to change a string to a list of characters.
lst = [i for i in 'Python']
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']
#For instance if you want to generate a list of numbers
numbers = [(i, i * i) for i in range(11)]
print(numbers)   # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
#List comprehension can be combined with if expression
# Filter numbers: let's filter out positive even numbers from the list below
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Lambda function does not use return but it explicitly returns the expression.
# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
#Using a lambda function inside another function.
def power(x):
    return lambda n : x ** n
cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32

"""Higher Order Functions"""
#Function as a Parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<
def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
#Function as a Return Value
def square(x):          # a square function
    return x ** 2
def cube(x):            # a cube function
    return x ** 3
def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)
def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
#Python Closures
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
#Python Decorators
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
#Applying Multiple Decorators to a Single Function
# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
#Accepting Parameters in Decorator Functions
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters
@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))
print_full_name("Asabeneh", "Yetayeh",'Finland') #I am Asabeneh Yetayeh. I love to teach. I live in Finland
#The map() function is a built-in function that takes a function and iterable as parameters.
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
#The filter() function calls the specified function which returns boolean for each item of the specified iterable (list).
# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False
long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']

"""Classes and objects"""
#The init constructor function has self parameter which is a reference to the current instance of the class
class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name =name
p = Person('Asabeneh')
print(p.name) #Asabeneh
print(p)  #<__main__.Person object at 0x2abf46907e80>
#Let us add more parameters to the constructor function.
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname) #Asabeneh
print(p.lastname) #Yetayeh
print(p.age) #250
print(p.country) #Finland
print(p.city) #Helsinki
#Objects can have methods. The methods are functions which belong to the object.
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info()) #Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland
#Sometimes, you may want to have a default values for your object methods. If we give default values for
#  the parameters in the constructor, we can avoid errors when we call or instantiate our class without 
# parameters. Let's see how it looks:
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
p1 = Person()
print(p1.person_info()) #Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info()) #John Doe is 30 years old. He lives in Noman city, Nomanland.
#Method to Modify Class Default Values
#In the example below, the person class, all the constructor parameters have default values. In addition to
#  that, we have skills parameter, which we can access using a method. Let us create add_skill method to add
#  skills to the skills list.
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)
p1 = Person()
print(p1.person_info()) #Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info()) #John Doe is 30 years old. He lives in Noman city, Nomanland.
print(p1.skills) #['HTML', 'CSS', 'JavaScript']
print(p2.skills) #[]
#Using inheritance we can reuse parent class code. Inheritance allows us to define a class that inherits all
#  the methods and properties from parent class. The parent class or super or base class is the class which 
# gives all the methods and properties. Child class is the class that inherits from another or parent class.
#  Let us create a student class by inheriting from person class.
class Student(Person):
    pass
s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info()) #Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills) #['JavaScript', 'React', 'Python']
print(s2.person_info()) #Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills) #['Organizing', 'Marketing', 'Digital Marketing']
#Overriding parent method
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'
s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info()) #Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills) #['JavaScript', 'React', 'Python']
print(s2.person_info()) #Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills) #['Organizing', 'Marketing', 'Digital Marketing']



