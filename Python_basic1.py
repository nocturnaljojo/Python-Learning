Built-In-Functions + Methods¶
print(len('hellloooo'))
 # when using len it counts from 1 and not 0
9
greet = 'hellloooo'
print(greet[0:len(greet)])
hellloooo
String methods
quote= 'to be or not to be'
print(quote.upper())
# the upper function will work like a CAPS LOCK
TO BE OR NOT TO BE
quote= 'to be or not to be'
print(quote.capitalize())
# The capitalize function will capitalise the beginning of the sentence
To be or not to be
quote= 'to be or not to be'
print(quote.replace('be','me'))
​
to me or not to me
quote= 'to be or not to be'
print(quote.replace('be','me'))
​
print(quote)
to me or not to me
to be or not to be
quote = 'to be or not to be'
quote2 = quote.replace('be','me')
print(quote2)
​
print(quote)
to me or not to me
to be or not to be
Booleans
False
name = 'Jovilisi'
is_cool = False
​
is_cool = True
# gives the result of either True or False
​
print(bool(1))
# A boolean of 1 means True 
print(bool(0))
# A boolean of 0 means False 
True
False
Exercise : Type Conversation
s
name = 'Jovilisi'
age = 30
relationship_status =' single'
​
relationship_status = 'It\'s complicated'
print(relationship_status)
It's complicated
birth_year = input('what year were you born? ')
what year were you born? 1991
age = 2023 - int(birth_year)
print(f' your age is: {age}')
​
 your age is: 32
DEVELOPER FUNDAMENTALS
# Booleans
name = 'Jovilisi'        # This assigns to a variable
is_cool = False
​
is_cool = True
​
print(bool('True'))
Password Checker
username = input('What is your username?')
​
password = input('What is your password?')
​
​
​
print(f'{username}, your password, {password}, is {len(password)} letters long')
What is your username?Jovilisi Draunimasi
What is your password?Jesus_my_Lord
Jovilisi Draunimasi, your password, Jesus_my_Lord, is 13 letters long
# When writing code make it easy to read
username = input('What is your username?')
​
password = input('What is your password?')
​
password_length = len(password)
hidden_password = '*' * password_length
​
​
print(f'{username}, your password, {hidden_password}, is {len(password)} letters long')
What is your username?Jovilisi Draunimasi
What is your password?Jesus_Is_My_Savior_and_Lord
Jovilisi Draunimasi, your password, ***************************, is 27 letters long
Lists
# Lists are like an array or a data structure
​
li  = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a',True]
​
print(li)
print(li2)
print(li3)
[1, 2, 3, 4, 5]
['a', 'b', 'c']
[1, 2, 'a', True]
amazon_cart = ['notebooks','sunglasses']
print(amazon_cart[0])
amazon_cart = ['notebooks','sunglasses']
print(amazon_cart[0])
​
notebooks
amazon_cart = ['notebooks','sunglasses']
print(amazon_cart[1])
amazon_cart = ['notebooks','sunglasses']
print(amazon_cart[1])
sunglasses
amazon_cart = ['notebooks','sunglasses']
print(amazon_cart[2])
amazon_cart = ['notebooks','sunglasses']
print(amazon_cart[2])
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_15904/1223855214.py in <module>
      1 amazon_cart = ['notebooks','sunglasses']
----> 2 print(amazon_cart[2])

IndexError: list index out of range

Just like strings, these list are stored
Slicing
- List Slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

#                [start:Finish:stepover]
print(amazon_cart[0::2])
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
​
#                [start:Finish:stepover]
print(amazon_cart[0::2])
['notebooks', 'toys']
um
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
​
#                [start:Finish:stepover]
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
['gum', 'sunglasses', 'toys']
['laptop', 'sunglasses', 'toys', 'grapes']
Matrix
)
matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
]
​
print(matrix[0][1])
2
List Methods part 1
basket = [1,2,3,4,5]
print(len(basket))
basket = [1,2,3,4,5]
print(len(basket))
5
basket = [1,2,3,4,5]


# adding
new_list = basket.append(100)
print(basket)
print(new_list)
basket = [1,2,3,4,5]
​
​
# adding
new_list = basket.append(100)
print(basket)
print(new_list)
​
# the append changes the list inplace
[1, 2, 3, 4, 5, 100]
None
basket = [1,2,3,4,5]


# adding
basket.append(100)
new_list = basket
print(basket)
print(new_list)
basket = [1,2,3,4,5]
​
​
# adding
basket.append(100)
new_list = basket
print(basket)
print(new_list)
[1, 2, 3, 4, 5, 100]
[1, 2, 3, 4, 5, 100]
Insert
basket = [1,2,3,4,5]


# adding
basket.insert(4,100)
new_list = basket
print(basket)
print(new_list)
basket = [1,2,3,4,5]
​
​
# adding
basket.insert(4,100)
new_list = basket
print(basket)
print(new_list)
[1, 2, 3, 4, 100, 5]
[1, 2, 3, 4, 100, 5]
basket = [1,2,3,4,5]


# adding
basket.insert(5,100)
new_list = basket
print(basket)
print(new_list)
basket = [1,2,3,4,5]
​
​
# adding
basket.insert(5,100)
new_list = basket
print(basket)
print(new_list)
[1, 2, 3, 4, 5, 100]
[1, 2, 3, 4, 5, 100]
basket = [1,2,3,4,5]


# adding

new_list = basket.insert(5,100)
print(basket)
print(new_list)
basket = [1,2,3,4,5]
​
​
# adding
​
new_list = basket.insert(5,100)
print(basket)
print(new_list)
[1, 2, 3, 4, 5, 100]
None
Extend
basket = [1,2,3,4,5]


# adding

new_list = basket.extend([100,101])
print(basket)
print(new_list)
basket = [1,2,3,4,5]
​
​
# adding
​
new_list = basket.extend([100,101])
print(basket)
print(new_list)
[1, 2, 3, 4, 5, 100, 101]
None
basket = [1,2,3,4,5]


# adding

new_list = basket.extend([100])
print(basket)
print(new_list)
basket = [1,2,3,4,5]
​
​
# adding
​
new_list = basket.extend([100])
print(basket)
print(new_list)
[1, 2, 3, 4, 5, 100]
None
Removing methods from a list
basket = [1,2,3,4,5]


# adding

new_list = basket.extend([100])

#print(new_list)

# removing
basket.pop()
print(basket)

# removes anything on the last column
basket = [1,2,3,4,5]
​
​
# adding
​
new_list = basket.extend([100])
​
#print(new_list)
​
# removing
basket.pop()
print(basket)
​
# removes anything on the last column
[1, 2, 3, 4, 5]
basket = [1,2,3,4,5]


# adding

new_list = basket.extend([100])

#print(new_list)

# removing
basket.pop()
basket.pop()
print(basket)

# removes anything on the last column
basket = [1,2,3,4,5]
​
​
# adding
​
new_list = basket.extend([100])
​
#print(new_list)
​
# removing
basket.pop()
basket.pop()
print(basket)
​
# removes anything on the last column
[1, 2, 3, 4]
basket = [1,2,3,4,5]


# adding

new_list = basket.extend([100])

#print(new_list)

# removing
basket.pop()
basket.pop(0) # removes the item in the index
print(basket)

# removes anything on the last column
basket = [1,2,3,4,5]
​
​
# adding
​
new_list = basket.extend([100])
​
#print(new_list)
​
# removing
basket.pop()
basket.pop(0) # removes the item in the index
print(basket)
​
# removes anything on the last column
[2, 3, 4, 5]
basket = [1,2,3,4,5]


# adding

new_list = basket.extend([100])

#print(new_list)

# removing
basket.remove(4) # removes the 4 from the list

print(basket)
basket = [1,2,3,4,5]
​
​
# adding
​
new_list = basket.extend([100])
​
#print(new_list)
​
# removing
basket.remove(4) # removes the 4 from the list
​
print(basket)
​
​
[1, 2, 3, 5, 100]
basket = [1,2,3,4,5]


# adding

new_list = basket.extend([100])

#print(new_list)

# removing
new_list = basket.remove(4) # removes the 4 from the list

print(new_list)
basket = [1,2,3,4,5]
​
​
# adding
​
new_list = basket.extend([100])
​
#print(new_list)
​
# removing
new_list = basket.remove(4) # removes the 4 from the list
​
print(new_list)
None
basket = [1,2,3,4,5]
​
​
# adding
​
new_list = basket.extend([100])
​
#print(new_list)
​
# pop
new_list = basket.pop(4)
​
print(new_list)
5
basket = [1,2,3,4,5]
basket = [1,2,3,4,5]
​
​
# adding
​
new_list = basket.extend([100])
​
#print(new_list)
​
# removing - using clear
new_list = basket.clear() # clears the entire basket
​
print(basket)
[]
List Method part 2
basket = [1,2,3,4,5]
print(basket.index(2))
basket = [1,2,3,4,5]
print(basket.index(2))
# Number 2 is in the index of 1 = when you count the list from [0 1 2 3 4]
#                                                     basket = [1,2,3,4,5]
# Similarly for the number 3, its index is 2
1
basket = ['a','b','c','d','e']
print(basket.index('d'))
basket = ['a','b','c','d','e']
print(basket.index('d'))
3
basket = ['a','b','c','d','e']
print(basket.index('d',0,2))
basket = ['a','b','c','d','e']
print(basket.index('d',0,2))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_15904/1677012355.py in <module>
      1 basket = ['a','b','c','d','e']
----> 2 print(basket.index('d',0,2))

ValueError: 'd' is not in list

basket = ['a','b','c','d','e']
print(basket.index('d',0,3))
basket = ['a','b','c','d','e']
print(basket.index('d',0,3))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_15904/2995279683.py in <module>
      1 basket = ['a','b','c','d','e']
----> 2 print(basket.index('d',0,3))

ValueError: 'd' is not in list

basket = ['a','b','c','d','e']
print(basket.index('d',0,4))
3
