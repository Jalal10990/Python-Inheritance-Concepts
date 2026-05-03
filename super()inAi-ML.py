
# parent class

class Model:
    def __init__(self, name):
        self.name = name
        self.trained = False
        print("Model constructor called")


# child class
class NeuralNetwork(Model):
    def __init__(self, name, layers):
        # call parent constructor
        super().__init__(name)

        self.layers = layers
        print("neiralNetwork constructor called")


# grandchild class

class CNN(NeuralNetwork):
    def __init__(self, name, layers, filters):
        # call parent constructor
        super().__init__(name, layers)

        self.filters = filters
        print("CNN constructor called")


# create object

cnn = CNN("ImageClassifier", [64, 32,10], 128)

print("\n--- Object Data ---")
print("Name     :", cnn.name)
print("Layers   :", cnn.layers)
print("Filters  :", cnn.filters)
print("Trained  :", cnn.trained)



        