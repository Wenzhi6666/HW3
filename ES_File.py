
import numpy as np

def ES(losses, alpha=None, VaR=None):
    """
    Calculate the Expected Shortfall (ES) of losses.
    
    :param losses: array of positively stated loss values
    :param alpha: risk level (e.g., 0.99 for 99%)
    :param VaR: dollar value or percentage specifying the VaR threshold
    :return: Expected Shortfall as the average of losses exceeding VaR
    """
'''
    es_value = 90
    return es_value
'''
if VaR is None:
    VaR = np.percentile(losses,100*confidence)
    tailloss = losses[losses>VaR]
    if len(tailloss)==0:
    return VaR  
    return np.mean(tailloss)
