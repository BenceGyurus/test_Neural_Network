from numpy import number
from open_File import *
from neuron_main import *
class test_Runner:
    def __init__(self, max_Of_Neurons, max_Of_Layers, max_Number_Of_Runs, number_Of_Testes):
        self.max_Of_Neurons = max_Of_Neurons
        self.max_Of_Layers = max_Of_Layers
        self.max_Number_Of_Runes = max_Number_Of_Runs
        self.networks = []
        self.number_Of_Layers = 0

    def main(self):
        for i in range(1, self.max_Of_Layers):
            self.number_Of_Layers = i
            for k in range(1, self.max_Of_Neurons):
                for j in range(0, self.max_Number_Of_Runes):
                    topology = [k for _ in range(i+2)]
                    topology[0] = len(self.open_Image(0,0))
                    topology[-1] = 10
                    self.create_Neural_Networks(topology)
                    self.teaching(j)

    def add_Sample(self):
        for i in range(0, 10):
            for k in range(0, 10):
                self.add_Inputs(self.open_Image(i,k))

    def run_Testes(self):
        pass

    def teaching(self,number_Of_Runes):
        self.target = [0 for i in range(0,10)]
        for _ in range(0, number_Of_Runes):
            for k in range(0, 10):
                for j in range(0, 10):
                    self.target[k] = 1
                    self.add_Inputs(self.open_Image(k,j))
                    self.backproagation(self.target)

    def backproagation(self, target):
        self.networks[0].backpropagation(target)
        self.networks[1].backpropagation2(target)

    def create_Neural_Networks(self, topology):
        self.networks = [neural_Network(topology, 0,0), neural_Network(topology, 0,0)]

    def add_Inputs(self, inputs):
        for network in self.networks:
            network.add_Inputs(inputs)

    def get_Results(self):
        return [network.get_Layer_Of_Neurons_Value(self.number_Of_Layers-1) for network in self.networks]

    def control_Results(self):
        pass

    def open_Image(self, folder, number):
        return open_Image(f"images/{folder}/{number}.png").open_File()

nn = test_Runner(10,1,1,1)
nn.main()
print(nn.get_Results())