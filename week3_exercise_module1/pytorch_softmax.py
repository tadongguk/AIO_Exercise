import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, input_tensor):
        input_exp = torch.exp(input_tensor)
        input_exp_sum = torch.sum(input_exp)
        softmax_output = input_exp / input_exp_sum
        return softmax_output


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, input_tensor):
        input_max = torch.max(input_tensor)
        input_exp = torch.exp(input_tensor-input_max)
        input_exp_sum = torch.sum(input_exp)
        softmax_output = input_exp / input_exp_sum
        return softmax_output


softmax = Softmax()
input_tensor = torch.tensor([1, 2, 3])
output = softmax(input_tensor)
print(output)
softmax = SoftmaxStable()
input_tensor = torch.tensor([1, 2, 3])
output = softmax(input_tensor)
print(output)
