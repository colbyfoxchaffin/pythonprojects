#--------Basic Data Types--------

#Numbers

print(1)       # int
print(1.0)     # float
print(1+1)     #Addition
print(1 * 3)   #Multi
print(1/2)     #Division
print(2 ** 4)  #Exponents
print(4 % 2)   #Modulus


#Variable Declaration
#Use '_' for multi word vars
var = 2
print(var)

#Strings
#Can use double or single quotes. Ex: "Hello", 'Hello'

#Printing Strings
x = 'hello'
print(x)

num = 12
name = 'Sam'

#Print Modifications
print('My number is {} and my name is {}'.format(num, name))

print('My number is {one} and my name is {two}'.format(one = num, two = name))

#Indexing Strings
s = 'abcdefghijk'
print(s[0])

#grab 'a' and beyond - Slice Syntax
print(s[0:])

#grab 'abc' (up to but not including index 3)
print(s[:3])

#grab 'def'
print(s[3:6])


# Lists
# A sequence of elements in '[]' separated by ','

my_list = ['a', 'b','c']
print(my_list)
#appending
my_list.append('d')
print(my_list)

print(my_list[1:3])

my_list[0] = 'NEW'

print(my_list)

#Can nest lists -> list in lists

nest = [1,2,[3,4]]
print(nest[2][1])

nest = [1,2,3,[4,5,['target']]]

print(nest[3][2][0])