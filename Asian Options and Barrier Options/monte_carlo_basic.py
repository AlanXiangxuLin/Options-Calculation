import numpy as np
from scipy.stats import norm

class MonteCarloOptionPricer:
    def __init__(self, S0, K, T, r, sigma, n_sims=10000):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.n_sims = n_sims
        
    def european_call(self):
        Z = np.random.standard_normal(self.n_sims)
        
        ST = self.S0 * np.exp((self.r - 0.5 * self.sigma**2) * self.T + 
                             self.sigma * np.sqrt(self.T) * Z)
        
        payoff = np.maximum(ST - self.K, 0)
        
        option_price = np.exp(-self.r * self.T) * np.mean(payoff)
        
        return option_price