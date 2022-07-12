import random
import math
class Connection:
    def __init__(self, connected_Neuron):
        self.connected_Neuron = connected_Neuron
        self.weight = random.uniform(0,1)
        self.last_Delta = 0
class Neuron:
    def __init__(self, last_Layer):
        self.learning_Rate = 0.3
        self.momentum = 0.01
        self.value = 0.0
        self.connections = []
        self.error = 0.0
        if last_Layer:
            for i in last_Layer:
                self.connections.append(Connection(i))
    def sigmoid(self,x):
        return 1/ (1 + math.exp(-x * 1.0))
    def derivated_Sigmoid(self,x):
        return x * (1-x)
    def feedforward(self):
        summed = 0
        for i in range(0, len(self.connections)):
            summed += self.connections[i].connected_Neuron.value*self.connections[i].weight
        self.value = self.sigmoid(summed)
    def cost_2(self):
        self.gradient = self.error * self.derivated_Sigmoid(self.value)
        for i in range(0, len(self.connections)):
            self.connections[i].d_Weight = self.eta * (self.connections[i].connected_Neuron.value * self.gradient)
            self.connections[i].d_Weight += self.learning_Rate * self.connections[i].d_Weight
            self.connections[i].weight += self.connections[i].d_Weight
            self.connections[i].connected_Neuron.error += self.connections[i].weight * self.gradient
    def cost(self):
        delta = self.error * self.value * (1 - self.value)
        for connection in self.connections:
            connection.weight += self.learning_Rate * delta * connection.connected_Neuron.value
            if connection.last_Delta:
                connection.weight += self.momentum*connection.last_Delta
            connection.last_Delta = delta
            connection.connected_Neuron.error += delta
        self.error = 0
class Network:
    def __init__(self, topology):
        self.all_Of_Layer = []
        for i in range(0, len(topology)):
            self.all_Of_Layer.append([])
            for k in range(0, topology[i]):
                if len(self.all_Of_Layer) > 1:
                    self.all_Of_Layer[i].append(Neuron(self.all_Of_Layer[-2]))
                else:
                    self.all_Of_Layer[i].append(Neuron(False))
    def load_Inputs(self, inputs):                                    #The inputs are binary numbers like 0 and 1
        for i in range(0, len(self.all_Of_Layer[0])):
            self.all_Of_Layer[0][i].value = inputs[i]  
    def feedforward(self):
        for i in range(1, len(self.all_Of_Layer)):
            for k in range(0, len(self.all_Of_Layer[i])):
                self.all_Of_Layer[i][k].feedforward()
    def backpropagation(self, target):                                  #type of target is list and number of element equal to the topology list last element and target list includes binary numbers like 0 and 1
        for i in range(0, len(target)):
            self.all_Of_Layer[-1][i].error = target[i] - self.all_Of_Layer[-1][i].value
        index = len(self.all_Of_Layer)-1
        while index:
            for i in range(0, len(self.all_Of_Layer[index])):
                self.all_Of_Layer[index][i].cost()
            index-=1
    def backpropagation2(self,target):
        for i in range(0, len(target)):
            self.all_Of_Layer[-1][i].error = target[i] - self.all_Of_Layer[-1][i].value
        index = len(self.all_Of_Layer)-1
        while index:
            for i in range(0, len(self.all_Of_Layer[index])):
                self.all_Of_Layer[index][i].cost_2()
            index-=1
class neural_Network:
    def __init__(self, topology, learning_Rate, eta):
        self.network = Network(topology)
    def add_Inputs(self, inputs):
        self.network.load_Inputs(inputs)
    def get_All_Of_Values(self):                #it return all outputs in the neural network
        return [[self.network.all_Of_Layer[i][k].value for k in range(0, len(self.network.all_Of_Layer[i]))] for i in range(0, len(self.network.all_Of_Layer))]
    def get_Layer_Of_Neurons_Value(self, layer_Number):        #it return all outputs of neuron in this layer what we give to layer_Number
        return [self.network.all_Of_Layer[layer_Number][i].value for i in range(0, len(self.network.all_Of_Layer[layer_Number]))]
    def feedforward(self):
        self.network.feedforward()
    def backpropagation(self, target):
        self.network.backpropagation(target)
    def backpropagation2(self,target):
        self.network.backpropagation2(target)