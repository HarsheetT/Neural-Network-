import numpy as np

inputs = [[1,2,3,2.5],
          [2.0,5.0,-1.0,2.0],
          [-0.26,-0.27,0.17,-0.8]]

weights = [[0.2,0.8,-0.5,1.0],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]

bias = [2,3,0.5]

weights2 = [[0.1,-0.14,0.5],
           [-0.5, 0.12, -0.33],
           [-0.44, 0.73, -0.13]]

bias2 = [-1, 2, -0.5]

'''
Actual Operation being performed:
Single Output = (Input1*Weight(0,0) + Input2*Weight(0,1) + Input3*Weight(0,2) + Input4*Weight(0,4)) + Bias[0] 

Multiple Output => We just change the weights and bias

Multiple Output = (Input1*Weight(0,0) + Input2*Weight(0,1) + Input3*Weight(0,2) + Input4*Weight(0,4)) + Bias[0]
                  (Input1*Weight(1,0) + Input2*Weight(1,1) + Input3*Weight(1,2) + Input4*Weight(1,4)) + Bias[1]
                  (Input1*Weight(2,0) + Input2*Weight(2,1) + Input3*Weight(2,2) + Input4*Weight(2,4)) + Bias[2]
'''

# layer_outputs = []
# for neuron_weights,neuron_bias in zip(weights,bias):
#     neuron_output = 0
#     for n_inputs,weights in zip(inputs,neuron_weights):
#         neuron_output += n_inputs*weights
#     neuron_output += neuron_bias
#     layer_outputs.append(neuron_output)

# print(layer_outputs)

output = np.dot(inputs , np.array(weights).T) + bias