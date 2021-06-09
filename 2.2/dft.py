import math


def w(p, k, N):
    expression = 2.0 * math.pi / N * p * k
    return complex(math.cos(expression), -math.sin(expression))


def dft(signals):
    N = len(signals)
    spectrum = [0] * N

    for p in range(N):
        for k in range(N):
            spectrum[p] += w(p, k, N) * signals[k]

    return [abs(x) for x in spectrum]