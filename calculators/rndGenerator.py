import numpy as np

class rndGenerator:
    def __init__(self, seed=None):
        if seed is None:
            from datetime import datetime
            seed = datetime.now().microsecond
        self.seed = seed
        self.steps = None
        self.generated = None

    def linearCongruential(self, n, a=8404997, b = 1, M = 2**35):
        x = [self.seed]
        if M is None:
            M = self.seed + 111111111

        for i in range(n):
            x.append((a * x[i] + b) % M)

        self.steps = np.array(x[1:])
        self.generated = self.steps / M
