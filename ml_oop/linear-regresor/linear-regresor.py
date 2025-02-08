import numpy as np
from sklearn.linear_model import LinearRegression

class LinearRegressor:
    def __init__(self):
        self.model = LinearRegression()
        
    def train(self, X, y):
        self.model.fit(X, y)
        
    def predict(self, X):
        return self.model.predict(X)
    

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

regressor = LinearRegressor()
regressor.train(X, y)
print(regressor.predict(np.array([[3, 5]])))