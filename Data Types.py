'''
Text Type  (String)
'''

#s = "This is a single string"
#print(s)
#print(type(s))

#=========================

#s = """this is a multiline
#string example"""
#print(s)

#======================

# find a character by index
#s = 'string sample'
#print(s[5])

#slicing
#s = 'string sample'
#print(s[1:6])

#========================
#inmutable

#s = 'string sample'
#s[2] = 'o'
#print(s)
#You cannot change the string values with inmutable

'''
Numeric Type (Integer, Float, Complex)
'''
#Integer
#x = 1234534567459586
#print(type(x))

#Float
#accurate up to 15-16 decimal places#
#x = 0.12345678978965345677654
#print(type(x))
#print(x)

#complex numbers
#x = 1+2j
#print(type(x))
#used for complex mathematics




'''
Sequence Type (List, Tuple, Range)
'''
#homogenous
#List
#You can have different types of data within a list, integer, complex and string
#x = [10, 2.5, 'hello']
#print(x[2])
#print(x[1:3])

#mutable list
#x[2] = 'Python'
#print(x)
#It can be changed

#Tuple
#heterogenous
#tuple = ()
#tuple = ("cat", [4,3,2], (1,2,3))
#Again, can use different data types

#===========================

#both examples below are type tuples, without a comma makes it a string. Its a very subtle change so be vigilant
#tuple = ("hello",)
#print(type(tuple))


#=======================

#tuple = ("cat", [4,3,2], (1,2,3))
#print((tuple[2])

#===========================

#immutable

#tuple = ("cat", [4,3,2], (1,2,3))
#tuple[2] = 10
#print(tuple)
#When working with a list its mutable, a string is immutable, Tuple is immutable
#=====================#


#Range
#Sequencing, its always the number minus 1
#x = range(10)
#for n in x:
  #print(n)

#=========================
'''
Mapping Type (Dictionary)
'''
#dict is mutable
#Use when we are dealing with keys and values
#dict = {'name': 'Alfred' , 'age':35 , 'resident': 'Bournemouth' }
#print(dict['age'])
#print(dict.get('name'))

#dict['age'] = 26
#print(dict)
#useful for databases when you dont know what the index is

'''
Set Types
'''

#Empty Set having set = {} is an empty dict
#set = set()
#print(type(set))

#========================
#mixed data types ( all immutable )
#set = {3.2, "hi", (1,2,3)}
#print(type (set))
#TypeError 'set' object is not subscriptable
#print(set[0])

#========================
#no duplicates
#set = {3.2, "hi", (1,2,3), "hi"}
#print(set)

#=========================
#cannot have mutable (list) in a set or duplicate items
#set = {3.2, "hi", (1,2,3), [1,2,3]}
#TypeError: unhashable type: 'list' like the above error
#print(set)
#=========================

'''
Boolean Type (True or False)
'''
#boolean as numbers
#print(type(True))
#print(True == 1)
#print(False == 0)

#interesting logic
#print(True + True)

#not boolean operator
#print(not True)
#print(not False)

# and boolean operator
#True and False will always be False
#print( True and False)

#print( True and True)

#print (False and False)

#or boolean operator
#print (True or False)
#print (True or True)
#print (False or False)



