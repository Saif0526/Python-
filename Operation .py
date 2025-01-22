#Comparison Operators

#Equal		
x = 3
y = 3
print(x == y)

#Not equal	
x = 5
y = 3
print(x != y)
	
#Greater than	x > y
x = 5
y = 3
print(x > y)
	
#Less than	x < y
x = 5
y = 3
print(x < y)
	
#Greater than or equal to	x >= y
x = 5
y = 3
print(x >= y)
	
#Less than or equal to	x <= y
x = 5
y = 3
print(x <= y)

#Logical Operators

#and (Returns True if both statements are true)
x = 5
print(x > 3 and x < 10)

#or (Returns True if one of the statements is true)
x = 5
print(x > 3 or x < 4)

# not (Reverse the result, returns False if the result is true)
x = 5
print(not(x > 3 and x < 10))

#in (Returns True if a sequence with the specified value is present in the object)

x = ["apple", "banana"]

print("banana" in x)

#not in (Returns True if a sequence with the specified value is not present in the object)

x = ["apple", "banana"]

print("pineapple" not in x)