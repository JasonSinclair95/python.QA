#Sleep in
# The parameter weekday is True if it is a weekday, and the parameter vacation is 
# True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. 
# Return True if we sleep in. wronge compared to example

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  if vacation:
    return True
  elif vacation:
    return True
  else:
    False

# monkey trouble
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or if neither of them is smiling. 
# Return True if we are in trouble. wronge compared to example

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif a_smile and b_smile:
    return True
  else:
    return False

#Sum_double
# Given two int values, return their sum. 
# Unless the two values are the same, then return double their sum.
def sum_double(a, b):
  num = a + b
  if a != b:
    return num
  elif a == b:
    return num *2

# diff21
#Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

def diff21(n):
  if n <=21:
    return 21 - n
  if n>=21:
    return (n - 21) * 2


