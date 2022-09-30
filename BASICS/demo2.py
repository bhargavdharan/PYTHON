# Python Variables

a = 22

print(a) # 22
print(type(a)) # <class 'int'>

b = int(22) # casting

print(b)

c = str(22)

print(c)
print(type(c)) # <class 'str'>

# many varaibles to multiple values
x,y,z = "apple","grapes","mango"

print(x)
print(y)
print(z)
print(x,y,z)

# many varaibles to only one value
x=y=z= "ram"

print(x)
print(y)
print(z)

# conversion of integer type data to float type data

a1 = 20 # int 
print(type(a1))
x1 = float(a1) # float
print(type(x1))

a2 = 2
print(a2)
print(type(a2))

b2 = a2
print(float(b2))
b2 = float(a2)
print(type(b2))

