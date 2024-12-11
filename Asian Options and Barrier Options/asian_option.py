import numpy as np

class AsianOptionPricer:
    def __init__(self, S0, K, T, r, sigma, n_steps=252, n_sims=10000):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.n_steps = n_steps
        self.n_sims = n_sims
        self.dt = T/n_steps
        
    def simulate_paths(self):
        Z = np.random.standard_normal((self.n_sims, self.n_steps))
        S = np.zeros((self.n_sims, self.n_steps + 1))
        S[:, 0] = self.S0
        
        for t in range(1, self.n_steps + 1):
            S[:, t] = S[:, t-1] * np.exp((self.r - 0.5 * self.sigma**2) * self.dt + 
                                        self.sigma * np.sqrt(self.dt) * Z[:, t-1])
        return S
    
    def price_asian_call(self):
        paths = self.simulate_paths()
        average_prices = np.mean(paths, axis=1)
        payoffs = np.maximum(average_prices - self.K, 0)
        option_price = np.exp(-self.r * self.T) * np.mean(payoffs)
        return option_price