from neurotech_network import NeuralNetwork


def build_simple_model():
    # Define the structure of the neural network model here
    pass


train_images = ...
train_labels = ...
val_images = ...
val_labels = ...

nn = NeuralNetwork()  # Create an instance of the NeuralNetwork class
nn.build_and_train((train_images, train_labels), (val_images, val_labels))
