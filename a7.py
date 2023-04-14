from neural import *

xor_data = [
    ([0,0],[0]),
    ([0,1], [1]),
    ([1,0], [1]),
    ([1,1], [0]),]

orn = NeuralNet(2, 3, 1)
orn.train(xor_data)

print(orn.test_with_expected(xor_data))

party_data = [
    ([0.9, 0.6, 0.8, 0.3, 0.1],[1.0]),
    ([0.8, 0.8, 0.4, 0.6, 0.4],[1.0]),
    ([0.7, 0.2, 0.4, 0.6, 0.3],[1.0]),
    ([0.5, 0.5, 0.8, 0.4, 0.8],[0.0]),
    ([0.3, 0.1, 0.6, 0.8, 0.8],[0.0]),
    ([0.6, 0.3, 0.4, 0.3, 0.6],[0.0]),]

partyn = NeuralNet(5, 3, 1)
partyn.train(party_data)

print(partyn.test_with_expected(party_data))