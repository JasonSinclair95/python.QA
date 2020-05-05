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

#parrot_ toruble 
#We have a loud talking parrot. 
# The "hour" parameter is the current hour time in the range 0..23. 
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
  if talking and (hour <7 or hour >20):
    return True
  else: 
    return False

#makes10
#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
  if a + b == 10:
    return True
  if a == 10 or b == 10:
    return True
  else:
    return False

#Given an int n, return True if it is within 10 of 100 or 200. 
# Note: abs(num) computes the absolute value of a number
def near_hundred(n):
  if abs(100 -n) <=10:
    return True
  if abs(200-n) <= 10:
    return True
  else:
    return False

#pos negative
#Given 2 int values, return True if one is negative and one is positive. 
# Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
  if negative:
    if a <= 0 and b <=0:
     return True
    else:
      return False
  if negative == False:
    if (a >= 0 and b <=0) or (a <= 0 and b >=0):
      return True
    else:
      return False
  
  # not_string
  #Given a string, return a new string where "not " has been added to the front. 
  # However, if the string already begins with "not", return the string unchanged.
  def not_string(str):
  if str[0:3] =='not':
    return str
  else:
    return "not " + str

#missinf_char
#Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string 


 def missing_char(str, n):
  letter = str[n]
  str = str.replace(letter, "")
  return str

# front_back
#Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
  if len(str)<= 1:
    return str
  mid = str[1:-1]
  front = str[-1]
  back = str[0]
  return front + mid + back

#front3
#Given a string, we'll say that the front is the first 3 chars of the string. 
# If the string length is less than 3, the front is whatever is there. 
# Return a new string which is 3 copies of the front.
def front3(str):
  front = str[0:3]
  if len(str) < 1:
    return str
  else:
    return front * 3