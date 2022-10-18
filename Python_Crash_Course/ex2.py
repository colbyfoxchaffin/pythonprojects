#Basic Data Types Pt 2

#Dictionaries

from cgi import print_arguments


d = {'key1' : 'value', 'key2': 123}

print(d['key1'])

print(d['key2'])

d = {'k1':[1,2,3]}

print(d['k1'])

my_list = d['k1']

print(my_list[0])

print(d['k1'][0])

d = {'k1':{'innerkey': [1,2,3]}}

print(d['k1']['innerkey'][1])

#Booleans
#True, False (Always capitalized)

my_list = [1,2,3]
my_list[0]


#tuples use parens not brackets
t = (1,2,3)

print(t[0])

#Tuples are immutable - cannot be changed

my_list[0] = "NEW"

print(my_list)

#Sets - a collection of UNIQUE elements

{1,2,3}

{1,1,1,1,2,2,2,3,3,3,3}

#Will only print {1,2,3}
print({1,1,1,1,2,2,2,3,3,3,3})

#create a set 
print(set([1,1,1,2,2,2,3,3,3]))


s = {1,2,3}
s.add(5)

print(s)

#Comparison Operators

print(1 > 2)
print(2 == 2)
print(1!=3)

#can compare strings
print('hi' == 'bye') #False

print(1 < 2 and 2 < 3) #True

print(1 < 2 or 2 > 3) #True

if 1<2: 
    print('yep!')

if True:
    print('Perform Code')

#Check for multiple conditions

if 1 == 2:
    print('First')
elif 3==3:
    print('middle')
else: 
    print('last')


#For Loops

seq = [1,2,3,4,5]

for item in seq:
    print(item)

#While loop

i = 1

while i < 5:
    print('i is:{}'.format(i))
    i = i + 1


#Using Range
for x in range(0,5):
    print(x)

range(0,5)


#List Comprehension
x = [1,2,3,4]
out = []

for item in x:
    out.append(item ** 2)

print(out)

#Translate the above into list comprehension
print([item ** 2 for item in x])

#Functions
def my_func(name):
    print('Hello ' + name)

my_func('Colby')

def square(num):
    """
    DocString this can be whatever I want over multiple lines
    This function squares a number
    """
    return num ** 2

output = square(2)
print(output)

#Map and Filter Functions

def times2(var):
    return var * 2

#map()

seq = [1,2,3,4,5]

print(map(times2,seq))
print(list(map(times2,seq)))

#lambda expression
#rewrite times2 as a lambda
print(list(map(lambda var: var*2, seq)))

#built-in filter function
#filter based on conditional True/Flase
print(list(filter(lambda num: num%2 ==0, seq)))


#Methods - calls to make off of an object
s = 'hello my name is Colby'
print(s.lower())
print(s.upper())
print(s.split())

tweet = 'go sports! #Sports'

print(tweet.split('#'))
print(tweet.split('#')[1])

d = {'k1': 1, 'k2': 2}
print(d.keys())
print(d.items())

lst = [1,2,3]
print(lst.pop())
lst = [1,2,3,4,5]
item = lst.pop()
print(item)

#'In' Operator

print('x' in [1,2,3])

print('x' in ['x','y','z'])

#Tuple Unpacking

x = [(1,2),(3,4),(5,6)]

for item in x:
    print(item)

for (a,b) in x:
    print(a)

for a,b in x:
    print(b)