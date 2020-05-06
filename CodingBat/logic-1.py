
#When squirrels get together for a party, they like to have cigars. 
# A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
# Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
# Return True if the party with the given values is successful, or False otherwise.
def cigar_party(cigars, is_weekend):
  if is_weekend and cigars >=40:
    return True
  if not is_weekend and cigars in range(40,61):
    return True
  else:
    return False

#You and your date are trying to get a table at a restaurant. 
# The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. 
# The result getting the table is encoded as an int value with 0=no, 
# 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). 
# With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
def date_fashion(you, date):
  if you <=2 or date<=2:
    return 0
  if you >=8 or date >=8 :
    return 2
  else:
    return 1
  
  #The squirrels in Palo Alto spend most of the day playing. 
  # In particular, they play if the temperature is between 60 and 90 (inclusive). 
  # Unless it is summer, then the upper limit is 100 instead of 90. 
  # Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
def squirrel_play(temp, is_summer):
  if is_summer and temp in range(60,101):
    return True
  if not is_summer and temp in range(60,91):
    return True
  else:
    return False

  #Given 2 ints, a and b, return their sum. However, 
  # sums in the range 10..19 inclusive, 
  # are forbidden, so in that case just return 20.
  def sorta_sum(a, b):
  
  if a + b in range(10,20):
    return 20
  if a + b <=9:
    return a + b
  else: 
    return a+b

#Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, 
# and a boolean indicating if we are on vacation, return a string of the form "7:00" 
# indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" 
# and on the weekend it should be "10:00". Unless we are on vacation -- 
# then on weekdays it should be "10:00" and weekends it should be "off".
def alarm_clock(day, vacation):
  if vacation and day == 0:
    return 'off'
  if vacation and day == 6:
    return 'off'
  if vacation and day in range(1,6):
    return '10:00'
  if not vacation and day in range(1,6):
    return "7:00"
  if not vacation and day == 0 or day ==6:
    return '10:00'
  
  #The number 6 is a truly great number. 
  # Given two int values, a and b, return True if either one is 6. 
  # Or if their sum or difference is 6. 
  # Note: the function abs(num) computes the absolute value of a number.

  def love6(a, b):
  if a == 6 or b==6:
    return True
  if a + b == 6:
    return True
  if b + a == 6:
    return True
  if a - b ==6:
    return True
  if b - a ==6:
    return True 
  else:
    return False

# Given a number n, return True if n is in the range 1..10, inclusive. 
# Unless outside_mode is True, in which case return True if the number is less or equal to 1,
#  or greater or equal to 10.
def in1to10(n, outside_mode):
  if n in range(1,11) and not outside_mode:
    return True
  if n >=11 and not outside_mode:
    return False
  if outside_mode and n<= 1 or n>=10:
    return True
  else:
    return False

#Given a non-negative number "num", return True if num is within 2 of a multiple of 10. 
# Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: 
# Introduction to Mod

def near_ten(num):

    a = num % 10
    if  (10 - (10-a)) <= 2 or (10 - a) <= 2:
        return True
    else:
        return False
