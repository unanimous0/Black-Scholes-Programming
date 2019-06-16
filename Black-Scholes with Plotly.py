import numpy as np
import scipy.stats as stat

def europian_option(S, K, T, r, sigma, option_type):    # T: Time to maturity (T-t), r: Risk-Free rate
    d1 = (np.log(S/K) + (r+0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))

    if option_type == 'call':
        V = S * stat.norm.cdf(d1) - K * np.exp(-r*T) * stat.norm.cdf(d2)    # CDF(Cumulative Distribution Function, 누적분포함수)
    elif option_type == 'put':
        V = -S * stat.norm.cdf(-d1) + K * np.exp(-r*T) * stat.norm.cdf(-d2)

    return V


# Increase in the price of a security - Call option
print("Case 1-1. When the price of security Increases -> The price of a Call option")
print(europian_option(105, 100, 1, 0.02, 0.2, 'call'))

# Decrease in the price of a security - Call option
print("Case 1-2. When the price of security Decreases -> The price of a Call option")
print(europian_option(95, 100, 1, 0.02, 0.2, 'call'))

# Increase in the price of a security - Put option
print("Case 2-1. When the price of security Increases -> The price of a Put option")
print(europian_option(105, 100, 1, 0.02, 0.2, 'put'))

# Decrease in the price of a security - Put option
print("Case 2-2. When the price of security Decreases -> The price of a Put option")
print(europian_option(95, 100, 1, 0.02, 0.2, 'put'))


# To show the dynamic variation of the optoin price -> Use Plotly library
# (Especially to show the variation of the option price, when the underlying asset and maturity change.)
# This library Interactively shows the variation with a 3D Graph. 
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)  # To choose whether to show the graph into the jupyter notebook or IDE

def Variation_of_Call_Option_Price():
    # Parameters
    K = 100
    r = 0.01
    sigma = 0.25

    # Variables - Time to Maturity & The price of an underlying asset
    T = np.linspace(0,1,100)
    S = np.linspace(0,200,100)
    T, S = np.meshgrid(T,S)

    # Output
    Call_Value = europian_option(S, K, T, r, sigma, 'call')

    trace = go.Surface(x=T, y=S, z=Call_Value)  # go.Surface: the function of Plotly to use the 3D Surface
    data = [trace]  # Make trace as list
    layout = go.Layout(title="Call Option",
                       scene={'xaxis':{'title':'Time to Maturity'}, 'yaxis':{'title':'Spot Price'}, 'zaxis':{'title':'Option Price'}})
    fig = go.Figure(data=data, layout=layout)
    return iplot(fig)


def Variation_of_Put_Option_Price():
    # Fixed value
    K = 100
    r = 0.01
    sigma = 0.25

    # Variables
    # The reason to make only T and S an array is that only the both variables change. 
    # - The other variables have a fixed value.
    T = np.linspace(0,1,100)
    S = np.linspace(0,200,100)
    T, S = np.meshgrid(T,S)

    # Output
    Put_Value = europian_option(S, K, T, r, sigma, 'put')

    trace = go.Surface(x=T, y=S, z=Put_Value)  # go.Surface: the function of Plotly to use the 3D Surface
    data = [trace]  # Make trace as list
    layout = go.Layout(title="Put Option",
                       scene={'xaxis':{'title':'Time to Maturity'}, 'yaxis':{'title':'Spot Price'}, 'zaxis':{'title':'Option Price'}})
    fig = go.Figure(data=data, layout=layout)
    return iplot(fig)

Variation_of_Call_Option_Price()
Variation_of_Put_Option_Price()