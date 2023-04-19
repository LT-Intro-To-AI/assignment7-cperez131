from neural import *

xor_data = [
    ([0,0],[0]),
    ([0,1], [1]),
    ([1,0], [1]),
    ([1,1], [0]),
]

orn = NeuralNet(2, 3, 1)
orn.train(xor_data)

print(orn.test_with_expected(xor_data))

xor2_data = [
    ([0,0],[0]),
    ([0,1], [1]),
    ([1,0], [1]),
    ([1,1], [0]),
]

orn2 = NeuralNet(2, 1, 1)
orn2.train(xor_data)

print(orn2.test_with_expected(xor2_data))

# party_data = [
#     ([0.9, 0.6, 0.8, 0.3, 0.1],[1.0]),
#     ([0.8, 0.8, 0.4, 0.6, 0.4],[1.0]),
#     ([0.7, 0.2, 0.4, 0.6, 0.3],[1.0]),
#     ([0.5, 0.5, 0.8, 0.4, 0.8],[0.0]),
#     ([0.3, 0.1, 0.6, 0.8, 0.8],[0.0]),
#     ([0.6, 0.3, 0.4, 0.3, 0.6],[0.0]),]

# partyn = NeuralNet(5, 6, 1)
# partyn.train(party_data)

# print(partyn.test_with_expected(party_data))

# test_data = [
#     [1, 1, 1, .1, .1],
#     [.5, .2, .1, .7, .7],
#     [.8, .3, .3, .3, .8],
#     [.8, .3, .3, .8, .3],
#     [.9, .8, .8, .3, .6]
# ]

# for x in range(5):
#     print(f"case {x+1}: {test_data[x]} evaluates to: {partyn.evaluate(test_data[x])}")
#     eval = partyn.evaluate(test_data[x])
#     print(eval)
#     # if int(partyn.evaluate(test_data[x]) )> .6:
#     #     print(" Republican")
#     # elif int(partyn.evaluate(test_data[x])) < .4:
#     #     print(" Democratic")
#     # else:
#     #     print( "Neutral")

