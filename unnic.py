import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
  return 1 / (1+np.exp(-x))

x = np.random.randn(1000, 100)
node_num = 100
hidden_layer_size = 5
activations = {}

for i in range(hidden_layer_size):
  if i != 0:
    x = activations[i-1]

  w = np.random.randn(node_num, node_num) / np.sqrt(node_num)*1
  a=np.dot(x,w)
  z = sigmoid(a)
  activations[i] = z