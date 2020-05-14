import random
from random import choice
import matplotlib.pyplot as plt 

list = [1,2]
x = random.choice(list)
y = random.choice(list)
print(x)
print(y)
plt.plot(x,y)
plt.show()