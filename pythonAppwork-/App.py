import random
from random import choice
import matplotlib.pyplot as plt 
import numpy as np 

list = [1,2]
x = random.choice(list)
y = random.choice(list)
print(x)
print(y)
plt.plot(x,y)
plt.show()

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x* (1-x)


training_input = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)
synaptic_weights = 2 * np.random.random((3,1))-1

print('random starting synaptic weights', synaptic_weights)


for iteration in range(50000):
    input_layer = training_input
    outputs = sigmoid(np.dot(input_layer,synaptic_weights))
    error = training_outputs - outputs
    adjustment = error * sigmoid_derivative(outputs)

    synaptic_weights += np.dot(input_layer.T,adjustment)

print('after train', synaptic_weights)
print('outputs ', outputs)