import torch
import torch.optim as optim
import torch.nn as nn
from torch.autograd import Variable
from network import Network


class FC(nn.Module):
    def __init__(self, in_size, out_size):
        super(FC, self).__init__()
        self.fc1 = nn.Linear(in_size, out_size,bias=False)
        self.softmax = nn.Softmax(1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.softmax(x)
        return x


def predicate(net, *input):
    d = torch.zeros(21)
    d[int(input[0])] = 1.0
    d = torch.autograd.Variable(d.unsqueeze(0))
    output = net.net(d)
    return output.squeeze(0)





network = FC(21, 2)
ND_net = Network(network, 'no_dealer_net', predicate)
ND_net.optimizer = optim.Adam(network.parameters(), lr=1.0)
