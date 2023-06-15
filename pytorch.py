import torch

x = torch.Tensor(3.5, requires_grad=True)
y = (x-1) * (x-2) * (x-3)
y.backward()