#Data Type

# 1. Numeric 

type(-12)
# int

type(12+10.50)
# float

type(12+4j)
#complex or imaginary

#Boolean 

type(1 > 4)
True or false

#Sequence 

#Strings

"single Quote"
"Duble Quote"
multiline = """ 
Today is Holiday,
we are going to market,
Buying some clothes,
for my self.
"""
print(multiline)
"""
'I've always wanted to  ear gallon of "ice cream"
"""
type(multiline)

a = 'Hello world'
print(a[6])

a*3
print(a)

#List 

[1,2,3,4,5]

['chocolate','vanilla','icecream']

ice_cream = ['tough','vanilla','chocolate']
ice_cream.append('salted caramel')
print(ice_cream)

# nested list

nest_list = ['vanilla',3,['scoop','spoon'],True]
nest_list[2] [1]
print(nest_list [2] [1])

#Tuples 
tuple_scoops = (1,2,3,5,5,4,3,2,1)
print(tuple_scoops)

#sets

daily_pints = (1,2,3)
print(daily_pints)

daily_pints_log = {1,2,3,5,2,6,9,12}
print (daily_pints_log )

Nik_daily_pints_log = {1,2,23,8,2,6,3,52}
print(daily_pints_log | Nik_daily_pints_log  )
#unique value
print(daily_pints_log & Nik_daily_pints_log )
# same value
print(daily_pints_log - Nik_daily_pints_log  )
# different value
print(daily_pints_log ^ Nik_daily_pints_log )
#either in one but not in both

# Dictionaries
# key/ value pair
