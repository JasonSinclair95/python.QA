#Question: Write a program which can compute the factorial of a given numbers. 
#The results should be printed in a comma-separated sequence on a single line. 
#Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

n = input("Enter a number: ")
factorial = 1
if factorial <= 1:
    print('factorials cant be less than one, please eneter another factorial number')
if int(n) >= 1:
    for i in range (1,int(n)+1):
        factorial = factorial * i

print("Factorail of ",n , " is : ",factorial)