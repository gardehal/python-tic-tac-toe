# from https://gist.github.com/miloharper/62fe5dcc581131c96276 / https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1

# $ python.exe -m pip install numpy
# $ python main.py

# The following example, from github linked above, takes the training_set_inputs and attempts to guess the correct value store in the training_set_outputs array.
# The answer is compared then the synaptic_weights are adjusted based on the answer.
# Finally, the last line prints the result of a new array that was not seen in the training_set_inputs, which should be 1.
# The pattern of the output is whatever the first number in the array is.

# from numpy import exp, array, random, dot
# training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 0], [0, 1, 1]])
# training_set_outputs = array([[0, 1, 1, 0]]).T
# random.seed(1)
# synaptic_weights = 2 * random.random((3, 1)) - 1
# for iteration in range(10000):
#     output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
#     synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
# print(1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights)))))


from numpy import exp, array, random, dot

class AI:
    def printExample():
        training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 0], [0, 1, 1]])
        training_set_outputs = array([[0, 1, 1, 0]]).T
        random.seed(1)
        synaptic_weights = 2 * random.random((3, 1)) - 1

        for iteration in range(10000):
            output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
            synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
            
        print(1 / (1 + exp(-(dot(array([1, 0, 1]), synaptic_weights)))))

    def aiTest():
        training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 0], [0, 1, 1]])
        training_set_outputs = array([[1, 1, 0, 1]]).T
        random.seed(1)
        synaptic_weights = 2 * random.random((3, 1)) - 1

        for iteration in range(10000):
            output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
            synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
            
        print(1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights)))))