# Neural-Network-
This repository explores the inner workings of neural networks by implementing one from scratch using Python libraries like NumPy.  pen_spark

<br>

## Day 1 - Building The Neuron
<p>
Today, we explored the building block of neural networks - the neuron!

<br>

#### Neurons 101:

They receive inputs (numbers) with associated weights (importance).
A bias acts like a constant nudge.
All these are combined and sent through an activation function to create the output.
<br> 

#### Learning with Weights & Biases:

By adjusting weights & biases, we change how the neuron reacts to inputs.
This allows the network to learn and produce the desired outputs over time.
<br>

#### In short: We control the neuron's output by playing with its internal settings! ️
</p>

## Day 2 - Building a Neuron with NumPy and Class
<p>
Yesterday, we explored the inner workings of a neuron. Today, we'll see how to code it efficiently using Python's NumPy library and create a class to organize the neuron's components.
<br>

#### Simplifying with NumPy:
We'll use numpy.dot() to perform the weighted sum of inputs and biases in a single line, making the code cleaner and faster.
<br>

#### Creating a Neuron Class:
We'll define a Python class to encapsulate the neuron's weights, biases, and functionality. This class will include a forward method that calculates the neuron's output based on the input it receives.
<br>

By combining NumPy and a class, we'll create a more organized and efficient representation of a neuron, paving the way for building neural networks!
</p>

## Day 3 - Activation_Functions and Loss

<p>
Today, we delve deeper into neural networks by exploring activation functions, calculating loss, and introducing the Softmax function.
<br>

#### Hidden Layer Activation Functions:

##### Linear: 
While simple, linear activation functions might not capture complex relationships in data.
<br>

##### ReLU (Rectified Linear Unit): 
A popular choice, ReLU introduces non-linearity, allowing the network to learn more intricate patterns. However, it can cause issues with "dying neurons" due to its insensitivity to negative inputs.
<br>

#### Softmax: The Activation for Multi-Class Classification

ReLU's limitation with negative numbers becomes crucial when dealing with multi-class classification problems. Here's where Softmax comes in.
Softmax takes the output from the final hidden layer and transforms it into an array of probabilities between 0 and 1, where each element represents the probability of the input belonging to a specific class.
<br>

#### Calculating Loss: Categorical Cross Entropy
To evaluate the performance of our network, we need to measure the difference between the predicted probabilities (from Softmax) and the actual labels.
Categorical Cross Entropy is a common loss function used for multi-class classification. It quantifies this difference, guiding the network's learning process towards producing more accurate probability distributions.
</P>