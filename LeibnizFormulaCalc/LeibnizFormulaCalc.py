def calculate_pi(iterations):
    pi_approximation = 0
    numerator = 4
    denominator = 1

    for i in range(1, iterations):
        sign = 2 * (i % 2) - 1
        pi_approximation += sign * numerator / denominator
        denominator += 2

    return pi_approximation

# Get the number of iterations from the user
num_iterations = int(input("Enter the number of iterations: "))

# Calculate the approximation of pi
approximation_of_pi = calculate_pi(num_iterations)

print(f"The approximation of pi after {num_iterations} iterations is: {approximation_of_pi}")