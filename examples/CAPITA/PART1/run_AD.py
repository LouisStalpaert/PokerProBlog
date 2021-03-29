from train import train_model
from model import Model
from network import Network
from standard_networks import FC
from data_loader import load
from optimizer import Optimizer
from examples.CAPITA.PART1.nets_AD import AD_net
import torch


train_queries = load('data/train_data.txt')
test_queries = load('data/test_data.txt')

#
# def neural_pred(network,i1,i2):
#     d = torch.zeros(20)
#     d[int(i1)] = 1.0
#     d[int(i2)+10] = 1.0
#     d = torch.autograd.Variable(d.unsqueeze(0))
#     output = network.net(d)
#     return output.squeeze(0)
#
#
# fc1 = FC(20,2)
# adam = torch.optim.Adam(fc1.parameters(), lr=0.5)
# swap_net = Network(fc1, 'no_dealer_net', neural_pred, optimizer=adam)


#with open('compare.pl') as f:
with open('ActiveDealer.pl') as f:
    problog_string = f.read()

model = Model(problog_string, [AD_net])
optimizer = Optimizer(model, 32)
train_model(model, train_queries, 1, optimizer,test_iter=20, test = lambda x: Model.accuracy(x, test_queries), snapshot_iter=10000)
