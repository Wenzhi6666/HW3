
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

'''
def VaR(r, alpha):
    
    # This function returns the left tail value
    # alpha = risk level
    # r = an array of stock returns
    # out = positively stated value of r at the 1-alpha percentile

    out = .01 # Calculate the percentile
    return abs(out)  # Return the absolute value of the calculated percentile
'''
    def VaR(r, confidence, principal=1):
    varpercentile = np.percentile(r, (1-confidence)*100)  
    out = abs(principal * varpercentile)  
    return out
