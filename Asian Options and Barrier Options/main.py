from monte_carlo_basic import MonteCarloOptionPricer
from asian_option import AsianOptionPricer
from barrier_option import BarrierOptionPricer

def main():
    S0 = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.2
    B = 130
    
    euro_pricer = MonteCarloOptionPricer(S0, K, T, r, sigma)
    euro_price = euro_pricer.european_call()
    print(f"European Option: {euro_price:.4f}")
    
    asian_pricer = AsianOptionPricer(S0, K, T, r, sigma)
    asian_price = asian_pricer.price_asian_call()
    print(f"Asian Option: {asian_price:.4f}")
    
    barrier_pricer = BarrierOptionPricer(S0, K, B, T, r, sigma)
    barrier_price = barrier_pricer.up_and_out_call()
    print(f"Barrier Option: {barrier_price:.4f}")

if __name__ == "__main__":
    main()
