#!/usr/bin/env python
# coding: utf-8


#1

for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))


#2


#fact(x) method to calculate factorial
def fact(x):
    if x == 0:
        return 1
    else:    
        return x * fact(x - 1)

x=int(input())

print (fact(x))


#3


## written as a series of key:value pairs within braces { }
n=int(input())
d=dict()

for i in range(1,n+1):
    d[i]=i*i
    print (d)
    


#4


values=input()
l=values.split(",")
t=tuple(l)
print (l)
print (t)


#5


class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print (self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()


#6


import math

c=50
h=30
value = []
items = [x for x in input().split(',')]
for d in x:
    value.append(str(int(round(math.sqrt(2*c*int(d)/h)))))

print (','.join(value))


#7


row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)


#8


items = [x for x in input().split(',')]
items.sort()
print (','.join(items))


#9


l = []
while True:
    s = str(input())
    if s:
        l.append(s.upper())
    else:
        break;

for sentence in l:
    print (sentence)


#10


s = input()
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))


# 11


value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print (','.join(value))



#12

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print (",".join(values))


#13

s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"])


#14


s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("UPPER CASE", d["UPPER CASE"])
print ("LOWER CASE", d["LOWER CASE"])


#15

a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print (n1+n2+n3+n4)

#16

values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))


#17

netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print (netAmount)

#18


import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print (",".join(value))



#19


l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print (sorted(l, key=itemgetter(0,1,2)))


#20


def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

            for i in reverse(100):
                print (i)


#21

import math
pos = [0,0]
while True:
    s = raw_input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print int(round(math.sqrt(pos[1]**2+pos[0]**2)))


#22

freq = {}   
line = raw_input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort()

for w in words:
    print ("%s:%d" % (w,freq[w]))
   

#23

def square(num):
    return num ** 2

print (square(2))
print (square(3))

#24

print (abs.__doc__)
print (int.__doc__)
print (raw_input.__doc__)

def square(num):
    '''Return the square value of the input number.
    
    The input number must be integer.
    '''
    return num ** 2

print (square(2))
print (square.__doc__)

#25

class Person:
    name = "Person"
    
    def __init__(self, name = None):
        self.name = name

jeffrey = Person("Jeffrey")
print ("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print ("%s name is %s" % (Person.name, nico.name))



#26

def SumFunction(number1, number2):
	return number1+number2

print (SumFunction(1,2))

#27

def printValue(n):
	print str(n)

printValue(3)


#28

def printValue(n):
	print str(n)

printValue(3)


#29
def printValue(s1,s2):
	print int(s1)+int(s2)

printValue("3","4")

#30

def printValue(s1,s2):
	print s1+s2

printValue("3","4") #34

#31

def printValue(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1>len2:
		print s1
	elif len2>len1:
		print s2
	else:
		print s1
		print s2
		

printValue("one","three")

#32

def checkValue(n):
	if n%2 == 0:
		print "It is an even number"
	else:
		print "It is an odd number"
		

checkValue(7)

#33

def printDict():
	d=dict()
	d[1]=1
	d[2]=2**2
	d[3]=3**2
	print d
		

printDict()


#34
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print d
		

printDict()

#35

def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for (k,v) in d.items():	
		print v
		
   #36
        def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for k in d.keys():	
		print k
		

printDict()

#37

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li
		

printList()

#39
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[:5]
		

printList()

#40

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[-5:]
		

printList()

#41
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[5:]
		

printList()

#42
def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print tuple(li)
		
printTuple()

#43
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print tp1
print tp2


#44
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if tp[i]%2==0:
		li.append(tp[i])

tp2=tuple(li)
print (tp2)

#45
s= raw_input()
if s=="yes" or s=="YES" or s=="Yes":
    print ("Yes")
else:
    print ("No")
    
  #46
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print (evenNumbers)

#48

li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print (squaredNumbers)

#49
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print (evenNumbers)

#50

evenNumbers = filter(lambda x: x%2==0, range(1,21))
print (evenNumbers)

#51

squaredNumbers = map(lambda x: x**2, range(1,21))
print (squaredNumbers)

#52

class American(object):
    @staticmethod
    def printNationality():
        print "America"

anAmerican = American()
anAmerican.printNationality()
American.printNationality()


#53

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print anAmerican
print aNewYorker

#54

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print aCircle.area()

#55

class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print aRectangle.area()

#56

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print aSquare.area()


#57
raise RuntimeError('something wrong')

#58

def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
except Exception, err:
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup')
    
    #59
    
    class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")

#60

import re
emailAddress = raw_input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print (r2.group(1))















