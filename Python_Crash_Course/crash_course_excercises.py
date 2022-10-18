#What is 7 to the power of 4?

print(7 ** 4)

#Split this string
#S = "Hi there Sam!"
#into a list

s = "Hi there Sam!"
res1 = list(s.split())
print(res1)

#Given the variables:
#planet = "Earth"
#diameter = 12742
#Use '.format()' to print the following string
#the diameter of Earth is 12742 kilometers

planet = 'Earth'
diameter = 12742

string1 = 'The diameter of {} is {}'.format(planet, diameter)
print(string1)

#Given this nested list, use indexing to grab the word "hello"

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
res2 = lst[3][1][2]
print(res2)

#given this nested dictionary rab the word 'hello'. Be prepared, this will be annoying/trciky
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
res3 = d['k1'][3]['tricky'][3]['target'][3]
print(res3)

#What is the main difference between a tuple and a list?

#ANSWER: A Tuple is immutable, unable to have it's values changed. You are able to add to a tuple though.

#Create a function that grabs the email website domain from a string inthe form:
#user@domain.com
#Ex: passing 'user@domain.com' would return 'domain.com'

def getDomain(string):
    res4 = list(string.split('@'))
    return res4[1]

print(getDomain('user@domain.com'))

#Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuartion being attached to the word dog, but DO account for capitilization

def hasDog(string):
    if 'dog' in string.lower():
        print(string.lower())
        res = True
        return res

print(hasDog('This dog runs faster than the other dog dude!'))

#Use lambda expressions and the filter() function to fileter out words from a list that don't start with the letter 's'. For example:

#seq = ['soup','dog','salad','cat','great']
#should be filtered down to: ['soup', 'salad']

seq = ['soup','dog','salad','cat','great']

print(list(filter(lambda word: word[0] == 's', seq)))



#Final Problem
#Your are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small Ticket","Big Ticket". If your speed is 60 or less, the result if "No Ticket". If speed is between 61 and 80 inclusive, the result it "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in theparameters of the function) -- n your birthday, your speed can be 5 higher in all cases.

is_birthday = True

def caught_speeding(speed, is_birthday):
    if speed < 60 or (is_birthday == True and speed <= 65):
        res = "No ticket"
        return res
    elif speed> 60 and speed < 80 or (is_birthday == True and speed <= 85):
        res = "Small ticket"
        return res
    elif speed >= 81 or (is_birthday == True and speed <=86):
        res = "Big Ticket"
        return res

print(caught_speeding(81, True))

print(caught_speeding(81, False))


