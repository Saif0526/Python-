# Converting Data Types 

#Conv String to int 
num_int = 7

type(num_int)

num_str = '7'

type(num_str)
nun_str_conv = int(num_str)
type(nun_str_conv)
num_sum = num_int + nun_str_conv
print(num_sum)

# Conv List,Set, Tuples

list_type = [1,2,3,4]

type(list_type)

type(tuple(list_type))

list_type = [1,2,3,4,4,3,2,1,4,3,3,4]
set(list_type)

type(set(list_type))

#Conv dict
dict_type = {'name' : 'Sanjii','age' : '21', 'Hair' : 'Black'}
type(dict_type)
dict_type.keys()
dict_type.values()
dict_type.items()
type(list(dict_type.keys()))

#Conv Strings to Lists

long_str = "l like to party"
list(long_str)
