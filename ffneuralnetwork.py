import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(42)
input_layer_neurons = 2
hidden_layer_neurons = 4
output_neurons = 1

wh = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
bh = np.random.uniform(size=(1, hidden_layer_neurons))
wout = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

for _ in range(10000):
    hidden_layer_input1 = np.dot(X, wh)
    hidden_layer_input = hidden_layer_input1 + bh
    hidden_layer_activations = sigmoid(hidden_layer_input)
    output_layer_input1 = np.dot(hidden_layer_activations, wout)
    output_layer_input = output_layer_input1 + bout
    output = sigmoid(output_layer_input)
    E = y - output
    slope_output_layer = sigmoid_derivative(output)
    slope_hidden_layer = sigmoid_derivative(hidden_layer_activations)
    d_output = E * slope_output_layer
    Error_at_hidden_layer = d_output.dot(wout.T)
    d_hidden_layer = Error_at_hidden_layer * slope_hidden_layer
    wout += hidden_layer_activations.T.dot(d_output) * 0.1
    bout += np.sum(d_output, axis=0, keepdims=True) * 0.1
    wh += X.T.dot(d_hidden_layer) * 0.1
    bh += np.sum(d_hidden_layer, axis=0, keepdims=True) * 0.1

print(output)
