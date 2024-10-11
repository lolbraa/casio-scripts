import math

def acosh(x):
    return math.log(x + math.sqrt(x * x - 1))

print(acosh(5))


def cosh(x):
    return (math.exp(x) + math.exp(-x)) / 2

print(cosh(5))


epsilon = 0.5
n = 4
Omega3dB = cosh((acosh( math.sqrt(10 ** 0.3 - 1) / epsilon)) / n)
print(Omega3dB)