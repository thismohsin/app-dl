import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.errors = []

    def activation_function(self, x):
        """Step function as activation"""
        return np.where(x >= 0, 1, 0)

    def fit(self, X, y):
        """Train the perceptron"""
        # Initialize weights and bias
        n_features = X.shape[1]
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.n_iterations):
            errors = 0
            
            # For each training example
            for xi, target in zip(X, y):
                # Calculate prediction
                prediction = self.predict(xi)
                
                # Update weights and bias if prediction is wrong
                error = target - prediction
                if error != 0:
                    self.weights += self.learning_rate * error * xi
                    self.bias += self.learning_rate * error
                    errors += 1
            
            self.errors.append(errors)
            
            # If no errors, perceptron has converged
            if errors == 0:
                break

    def predict(self, X):
        """Make predictions"""
        linear_output = np.dot(X, self.weights) + self.bias
        return self.activation_function(linear_output)

# Generate linearly separable data for AND gate
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # AND gate outputs

# Create and train perceptron
perceptron = Perceptron(learning_rate=0.1, n_iterations=100)
perceptron.fit(X, y)


# Plotting decision boundary

def plot_decision_boundary():
    plt.figure(figsize=(10, 6))
    
    # Plot training points
    plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='red', marker='o', label='0')
    plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='blue', marker='x', label='1')
    
    # Create grid to plot decision boundary
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                        np.arange(y_min, y_max, 0.02))
    
    # Calculate predictions for grid points
    Z = np.array([perceptron.predict(np.array([x, y])) 
                 for x, y in zip(xx.ravel(), yy.ravel())])
    Z = Z.reshape(xx.shape)
    
    # Plot decision boundary
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Perceptron Decision Boundary for AND Gate')
    plt.legend()
    
    # Show final weights and bias
    print(f"Final weights: {perceptron.weights}")
    print(f"Final bias: {perceptron.bias}")
    
    # Test predictions
    print("\nPredictions:")
    for xi, target in zip(X, y):
        pred = perceptron.predict(xi)
        print(f"Input: {xi}, Target: {target}, Prediction: {pred}")

# Plot results
plot_decision_boundary()

# Plot error convergence
plt.figure(figsize=(10, 6))
plt.plot(range(len(perceptron.errors)), perceptron.errors)
plt.xlabel('Iterations')
plt.ylabel('Number of Errors')
plt.title('Perceptron Learning Convergence')
