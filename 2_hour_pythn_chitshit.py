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
#Tuple is immutable if we want to modify a tuple we should change it to a list.
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
print(st) #{'item1', 'item7', 'item4', 'item6', 'item5', 'item8'}
st.clear() #{} or set()
del st 
#str.casefold() methods
string = "GEEKSFORGEEKS"
print("lowercase string: ",string.casefold()) # lowercase string: geeksforgeeks
# casefold() to check if a string is palindrome or not
str = 'geeksforgeeks'
str = str.casefold() # make it suitable for caseless comparison
rev_str = reversed(str) # reverse the string
if str == rev_str:  # check if the string is equal to its reverse
	print("palindrome")
else:
	print("not palindrome") # Terminal: not palindrome
# casefold() to count the number of each vowel in a string
v = 'aeiou'  # string of vowels
str = 'Hello, have you try geeksforgeeks?'  # change this value for a different result
str = str.casefold() # caseless comparisions
c = {}.fromkeys(v,0) # {'a': 1, 'e': 6, 'i': 0, 'o': 3, 'u': 1} ,dictionary with each vowel a key and value 0
for char in str: # count the vowels
		if char in c:
				c[char] += 1
print(c)   #{'a': 1, 'e': 6, 'i': 0, 'o': 3, 'u': 1}
#center(total length) method
string = "geeks for geeks"
new_string = string.center(24, '#')
print("After padding String is:", new_string) #After padding String is: ####geeks for geeks#####
#encode() method
string = 'GeeksforGeeks'
print(string.encode("ascii", "ignore")) # ignore error , Terminal:b'GeeksforGeeks'
print (string.encode('utf8', 'ignore')) # ignore error, Terminal:b'GeeksforGeeks'
print(string.encode("ascii", "replace")) # replace error, Terminal:b'GeeksforGeeks'
#string format_map() used to return a dictionary key’s value.
def chk_msg(n):	
	a = {'name':"George", 'mesg':n} # input stored in variable a.	
	print('{name} has {mesg} new messages'.format_map(a)) # use of format_map() function
chk_msg(10)   #George has 10 new messages
#string is isprintable()
string ='GeeksforGeeks\nname\nis\nCS portal'
newstring = ''
count = 0
for a in string:
	if (a.isprintable()) == False:
			count+= 1
			newstring+=' '
	else:
			newstring+= a
print(count) #3
print(newstring) #GeeksforGeeks name is CS portal
#string isspace() method 
string = 'My name is Ayush'
count=0
for a in string:
	if (a.isspace()) == True:
		count+=1
print(count) #3
string = 'My name is \n\n\n\n\nAyush'
count = 0
for a in string:
	if (a.isspace()) == True:
		count+=1
print(count) #8
#string lstrip()method
string = "geeks for geeks"
print(string.lstrip('ge')) #ks for geeks
#string partition() method
string = "pawan is a good"
print(string.partition('is ')) #('pawan ', 'is ', 'a good')
print(string.partition('bad ')) #('pawan is a good', '', '')
# Python3 code explaining rpartition()
string1 = "Geeks@for@Geeks@is@for@geeks"
string2 = "Sita is going to school"
print(string1.rpartition('@')) #('Geeks@for@Geeks@is@for', '@', 'geeks')
print(string2.rpartition('is')) #('', '', 'Sita is going to school')
# splitlines() in one line
print('India\nJapan\nUSA\nUK\nCanada\n'.splitlines()) #['India', 'Japan', 'USA', 'UK', 'Canada']
# of translate() method
# specifying the mapping using ASCII
translation = {103: None, 101: None, 101: None}
string = "geeks"
print("Original string:", string) #Original string: geeks
print("Translated string:",string.translate(translation)) #Translated string: ks
#zfill() method returns a copy of the string with ‘0’ characters padded to the leftside of the given string.
number = "6041"
print(number.zfill(8)) #00006041
number = "+6041"
print(number.zfill(8)) #+0006041
text = "--anything%(&%(%)*^"
print(text.zfill(20)) #-0-anything%(&%(%)*^
#string rsplit() method
word = 'geeks, for, geeks, pawan'
print(word.rsplit(', ', 0)) #['geeks, for, geeks, pawan']
print(word.rsplit(', ', 4)) #['geeks', 'for', 'geeks', 'pawan']
word = 'geeks for geeks'
print(word.rsplit(None, 1)) #['geeks for', 'geeks']
print(word.rsplit(None, 2)) #['geeks', 'for', 'geeks']
print('@@@@@geeks@for@geeks'.rsplit('@')) #['', '', '', '', '', 'geeks', 'for', 'geeks']
print('@@@@@geeks@for@geeks'.rsplit('@', 1)) #['@@@@@geeks@for', 'geeks']
print('@@@@@geeks@for@geeks'.rsplit('@', 3)) #['@@@@', 'geeks', 'for', 'geeks']
print('@@@@@geeks@for@geeks'.rsplit('@', 5)) #['@@', '', '', 'geeks', 'for', 'geeks']

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

"""Regular expressions:A regular expression or RegEx is a special text string that helps to find patternsin data.
A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re."""
#re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.

import re
txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I)
print(match)  #<re.Match object; span=(0, 15), match='I love to teach'>
span = match.span()
print(span)     # (0, 15)
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach

import re
txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None
##re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
span = match.span()
print(span)     # (100, 105)
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
#re.findall: Returns a list containing all matches
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches = re.findall('python', txt, re.I) # It returns list
print(matches)  # ['Python', 'python'] Since we are using re.I both lowercase and uppercase letters are included.

import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']
# re.sub() Replacing a Substring.#re.sub: Replaces one or many matches within a string
import re
txt = '''Python is the most beautiful language that a human being has ever created.I recommend python for a first programming language'''
match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

import re
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
matches = re.sub('%', '', txt)
print(matches) #I am teacher and  I love teaching. There is nothing as rewarding as educating and empowering people.
               #I found teaching more interesting than any other jobs. 
               #Does this motivate you to be a teacher?
#re.split: Takes a string, splits it at the match points, returns a list
import re
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # ['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating
                            # and empowering people.', 'I found teaching more interesting than any other jobs.',
                            #  'Does this motivate you to be a teacher?']
#Writing RegEx Patterns:[]: A set of characters
"""[a-c] means, a or b or c
[a-z] means, any letter from a to z
[A-Z] means, any character from A to Z
[0-3] means, 0 or 1 or 2 or 3
[0-9] means any number from 0 to 9
[A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
\: uses to escape special characters
\d means: match where the string contains digits (numbers from 0-9)
\D means: match where the string does not contain digits
. : any character except new line character(\n)
^: starts with
r'^substring' eg r'^love', a sentence that starts with a word love
r'[^abc] means not a, not b, not c.
$: ends with
r'substring$' eg r'love$', sentence that ends with a word love
*: zero or more times
r'[a]*' means a optional or it can occur many times.
+: one or more times
r'[a]+' means at least once (or more)
?: zero or one time
r'[a]?' means zero times or once
{3}: Exactly 3 characters
{3,}: At least 3 characters
{3,8}: 3 to 8 characters
|: Either or
r'apple|banana' means either apple or a banana
(): Capture and group"""
#Let us use square bracket to include lower and upper case
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
#If we want to look for the banana, we write the pattern as follows:
regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
#Escape character(\) in RegEx
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want
#One or more times(+)
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!
#Period(.)
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']
regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
#Zero or many times. The pattern could may not occur or it can occur many times.
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
#Zero or one time. The pattern may not occur or it may occur once.
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
#Quantifier in RegEx
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
#Cart ^ starts with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
#Cart ^ Negation
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']

