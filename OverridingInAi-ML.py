
# PARENT CLASS

class BaseModel:

    def fit(self):
        print("Base model training...")

    def predict(self):
        print("Base model prediction...")

    def save(self):
        print("Model saved successfully ✅")
# CHILD 1
class LinearRegression(BaseModel):

    # OVERRIDE fit()
    def fit(self):
        print("Linear Regression training with math formula")

    # OVERRIDE predict()
    def predict(self):
        print("Linear Regression predicting numbers")

# CHILD 2
class RandomForest(BaseModel):

    # OVERRIDE fit()
    def fit(self):
        print("Random Forest training many decision trees")

    # OVERRIDE predict()
    def predict(self):
        print("Random Forest voting predictions")

# CREATE OBJECTS
lr = LinearRegression()
rf = RandomForest()



# RUN METHODS

print("Linear Regression:")
lr.fit()
lr.predict()
lr.save()

print("\nRandom Forest:")
rf.fit()
rf.predict()
rf.save()