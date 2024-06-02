import random

num = random.random()
print(num)

num1 = random.uniform(1,100)
print(num1)

num2 = random.randint(1,100)
print (num2)

num3 = random.randrange(0,100,2)
print(num3)

numlist = random.sample(range(0,100), 3)
print(numlist)
