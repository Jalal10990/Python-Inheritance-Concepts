# Parent Class
class BaseEstimator:

    def __init__(self, name):
        self.name = name
        self.trained = False

    def save(self):
        print(self.name, "model saved successfully ")

    def summary(self):
        print("\n--- Model Summary ---")
        print("Model Name :", self.name)
        print("Trained    :", self.trained)


# Child 1
class LinearRegression(BaseEstimator):

    def __init__(self):
        super().__init__("Linear Regression")
        self.weight = 0
        self.bias = 0

    def fit(self, X, y):
        self.weight = 2
        self.bias = 1
        self.trained = True
        print("Linear Regression trained successfully ")

    def predict(self, X):
        predictions = []

        for x in X:
            result = self.weight * x + self.bias
            predictions.append(result)

        return predictions


# Child 2
class RandomForest(BaseEstimator):

    def __init__(self):
        super().__init__("Random Forest")
        self.trees = 100

    def fit(self, X, y):
        self.trained = True
        print("Random Forest trained with", self.trees, "trees ")

    def predict(self, X):
        predictions = []

        avg = sum(X) / len(X)

        for x in X:
            if x > avg:
                predictions.append(1)
            else:
                predictions.append(0)

        return predictions


# Child 3
class NeuralNetwork(BaseEstimator):

    def __init__(self):
        super().__init__("Neural Network")
        self.layers = [3, 5, 2]

    def fit(self, X, y):
        self.trained = True
        print("Neural Network trained successfully ")

    def predict(self, X):
        predictions = []

        for row in X:
            if sum(row) > 5:
                predictions.append(1)
            else:
                predictions.append(0)

        return predictions

# Create Objects

lr = LinearRegression()
rf = RandomForest()
nn = NeuralNetwork()

# Inherited methods

lr.save()
rf.save()
nn.save()

# Train models
lr.fit([1, 2, 3], [2, 4, 6])
rf.fit([1, 2, 3], [0, 1, 1])
nn.fit([[1, 2], [3, 4]], [0, 1])


# Predict

print("\nLinear Regression Prediction:")
print(lr.predict([10, 20, 30]))

print("\nRandom Forest Prediction:")
print(rf.predict([1, 5, 10, 15]))

print("\nNeural Network Prediction:")
print(nn.predict([[1, 2], [4, 5], [2, 1]]))



# Summary

lr.summary()
rf.summary()
nn.summary()