import math
import main

def percept(listx, listw, bias, cfunc):
#    print("Hello percept")
    result = 0.0
    totalsum = 0.0
    print("cfunc: " + cfunc)
    for i in range(len(listw)):
        totalsum += listw[i] * listx[i]
    totalsum -= bias
    if cfunc == "h":
        result = heavy(totalsum)
    elif cfunc == "r":
        result = relu(totalsum)
    elif cfunc == "i":
        result = identity(totalsum)
    elif cfunc == "t":
        result = tanh(totalsum)
    elif cfunc == "s":
        result = sigmoid(totalsum)
    else:
        print("An Unexpected Error.")
        print(ValueError)

    return result


def heavy(totalsum):
    if totalsum >= 0:
        return 1
    else:
        return 0.0
    
def relu(totalsum):
    if totalsum >= 0:
        return totalsum
    else:
        return 0.0
    
def identity(totalsum):
    return totalsum

def tanh(totalsum):
    return math.tanh(totalsum)

def sigmoid(totalsum):
    value = 1 / (1 + math.exp(-1 * totalsum))
    return value