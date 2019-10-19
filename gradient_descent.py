from gradients import linear_gradient, gradient_step
from linear_algebra import vector_mean
import random

inputs = [(x, 10 * x + 7) for x in range(-50, 50)]

def run():
    print("computing random values for theta")
    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    print("Generating learning rate at 0.001")
    learning_rate = 0.001

    for epoch in range(5000):
        grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
        theta = gradient_step(theta, grad, -learning_rate)
        print(f"epoch: {epoch}, theta: {theta}")

    slope, intercept = theta
    print(f"final slope at {slope} and intercept at {intercept}")
    assert 9.99 < slope < 10.11, "slope should be about 10"
    assert 6.9 < intercept < 7.1,"intercept should be about 7"

if __name__ == "__main__":
    run()
