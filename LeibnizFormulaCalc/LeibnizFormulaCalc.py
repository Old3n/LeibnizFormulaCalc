iteration = int(input("Enter the number of iterations: "))
def pi():
    pi = 0
    n = 4
    d = 1
    for i in range(1, iteration):
        a = 2 * (i % 2) - 1
        pi += a * n / d
        d += 2
    print(pi)

pi()
