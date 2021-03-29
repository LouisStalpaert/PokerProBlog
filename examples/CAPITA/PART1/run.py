from train import train_model
from model import Model
from network import Network
from standard_networks import FC
from data_loader import load
from optimizer import Optimizer
from examples.CAPITA.PART1.nets import ND_net
import torch


train_queries = load('data/train_data_no_dealer.txt')
test_queries = load('data/test_data_no_dealer.txt')


#with open('compare.pl') as f:
with open('NoDealer.pl') as f:
    problog_string = f.read()

model = Model(problog_string, [ND_net])
optimizer = Optimizer(model, 32)
train_model(model, train_queries, 3, optimizer,test_iter=20, test = lambda x: Model.accuracy(x, test_queries), snapshot_iter=10000)
