#!/usr/bin/env python
# coding: utf-8

# In[3]:


l=[]
for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))


# In[18]:


#fact(x) method to calculate factorial
def fact(x):
    if x == 0:
        return 1
    else:    
        return x * fact(x - 1)

x=int(input())

print (fact(x))


# In[27]:


## written as a series of key:value pairs within braces { }
n=int(input())
d=dict()

for i in range(1,n+1):
    d[i]=i*i
    print (d)
    


# In[29]:


values=input()
l=values.split(",")
t=tuple(l)
print (l)
print (t)


# In[32]:


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


# In[27]:


import math

c=50
h=30
value = []
items = [x for x in input().split(',')]
for d in x:
    value.append(str(int(round(math.sqrt(2*c*int(d)/h)))))

print (','.join(value))


# In[36]:


row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)


# In[33]:


items = [x for x in input().split(',')]
items.sort()
print (','.join(items))


# In[39]:


l = []
while True:
    s = str(input())
    if s:
        l.append(s.upper())
    else:
        break;

for sentence in l:
    print (sentence)


# In[1]:


s = input()
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))


# In[3]:


value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print (','.join(value))


# In[4]:


values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print (",".join(values))


# In[5]:


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


# In[7]:


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


# In[9]:


a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print (n1+n2+n3+n4)


# In[10]:


values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))


# In[12]:


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


# In[13]:


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


# In[ ]:


l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print (sorted(l, key=itemgetter(0,1,2)))


# In[17]:


def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

            for i in reverse(100):
                print (i)


# In[ ]:




