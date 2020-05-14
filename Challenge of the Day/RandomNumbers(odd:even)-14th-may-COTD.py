import random
#for even number
print(random.sample(range(100,201,2),5))

#for random numbers
print (random.sample([i for i in range(100,201) if i%2!=0], 5))
