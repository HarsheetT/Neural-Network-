import numpy as np
np.random.seed(0)

X = [[1,2,3,2.5],
     [2.0,5.0,-1.0,2.0],
     [-0.26,-0.27,0.17,-0.8]]

class Layer_Dense:
    def __init__ (self,n_inputs,n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4,5) #Layer_Dense(no.of_inputs,No.of_neurons to be created => Can be any number)
layer2 = Layer_Dense(5,2) # Here 5 is the input cause it takes the previous outputs and mae them the inputs so the output in the previous ones are 5.   

layer1.forward(X)
layer2.forward(layer1.output)
