# +
weight = 0.1

def neural_network(input, weight):
    prediction = input * weight
    return prediction
    


# -

# Using single input
number_of_toes = [8.5, 9.5, 10, 9]
input = number_of_toes[0]
pred = neural_network(input, weight)
print(pred)


# +
# Use multiple inputs
def w_sum(a, b):
    assert(len(a) == len(b))
    
    output = 0
    
    for i in range(len(a)):
        output += (a[i] * b[i])
    
    return output

weights = [0.1, 0.2, 0]

def neural_network(inputs, weights):
    pred = w_sum(inputs, weights)
    return pred

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

inputs = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(inputs, weights)

print(pred)
# +
# Using numpy for multiple inputs
import numpy as np
weights = np.array([0.1, 0.2, 0])

def neural_network(input, weights):
    pred = input.dot(weights)
    return pred
    
toes = np.array([8.5, 9.5, 9.9, 9.0])
wrlec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

input = np.array([toes[0], wrlec[0], nfans[0]])
pred = neural_network(input, weights)
print(pred)
# +
# Using one input for multiple outputs
weights = [0.3, 0.2, 0.9]

def ele_mul(number, vector):
    output = [0, 0, 0]
    assert(len(output) == len(vector))
    
    for i in range(len(vector)):
        output[i] = number * vector[i]
        
    return output

def neural_network(input, weights):
    pred = ele_mul(input, weights)
    return pred

wlrec = [0.65, 0.8, 0.8, 0.9]
input = wlrec[0]
    
pred = neural_network(input, weights)
print(pred)

# +
# Prediction with multiple inputs and outputs
weights = [
    [0.1, 0.1, -0.3],
    [0.1, 0.2, 0.0],
    [0.0, 1.3, 0.1]
]

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output

def vect_mat_mul(vect, matrix):
    assert(len(vect) == len(matrix))
    output = [0, 0, 0]
    
    for i in range(len(vect)):
        output[i] = w_sum(vect, matrix[i])
    
    return output

def neural_network(input, weights):
    pred = vect_mat_mul(input, weights)
    return pred

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]

pred = neural_network(input, weights)
print(pred)
