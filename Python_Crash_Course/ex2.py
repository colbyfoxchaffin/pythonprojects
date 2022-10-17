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