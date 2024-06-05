import math
def check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def activation_function(activation, x):
    if activation == "sigmoid":
        return 1 / (1 + math.exp(-x))
    elif activation == "relu":
        if x <= 0:
            return 0
        else:
            return x
    elif activation == "elu":
        if x <= 0:
            return 0.01 * (math.exp(x) - 1)
        else:
            return x
    else:
        return f"{activation} is not a valid activation function"

x = input("Enter X:")
while check(x) is False:
    x = input("X must be an integer. Please enter X:")


activation = input("Enter activation function (sigmoid/relu/elu) :")
result = activation_function(activation, float(x))
print(result)