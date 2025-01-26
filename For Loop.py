s = ["Hello", "World"]

# using for loop with string
for i in s:
    print(i)
for i in range(0, 10, 2):
    print(i)
    
 # Prints all letters except 'e' and 'o'

for i in 'Hello World':

    if i == 'e' or i == 'o':
        continue
    print(i)
    
for i in 'Hello World':

    # break the loop as soon it sees 'e'
    # or 'o'
    if i == 'e' or i == 'o':
        break

print(i)

for i in range(1, 6):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")
 #Nested For Loops
for i in range(1, 4):
	for j in range(1, 4):
		print(i, j)