import numpy as np

def soft_thresholding(x, lambda_):
    return np.sign(x) * np.maximum(np.abs(x) - lambda_, 0)

def proximal_gradient_method(A, b, lambda_, lr=0.01, max_iterations=1000, tolerance=1e-6):
    x = np.zeros(A.shape[1])
    for iteration in range(max_iterations):
        gradient = A.T @ (A @ x - b)
        x_new = x - lr * gradient
        x_new = soft_thresholding(x_new, lr * lambda_)

        if np.linalg.norm(x_new - x, ord=2) < tolerance:
            print(f"Converged in {iteration + 1} iterations.")
            break
        x = x_new
    return x

np.random.seed(0)
A = np.random.randn(100, 20)
b = np.random.randn(100)
lambda_ = 0.1

x_solution = proximal_gradient_method(A, b, lambda_)

print("Solution vector x:", x_solution)
