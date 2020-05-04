import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
from sklearn.preprocessing import scale
from matplotlib.figure import Figure
from TFANN import ANNR

class Predict(object):
    def __init__(self, data, hidden, iterations, tolerance):
        df = pd.read_csv(data, skiprows = 1, usecols=(1,4))
        self.stock = scale(df)
        self.hidden = hidden
        self.iterations = iterations
        self.tolerance = tolerance
        
    def predictGraphByDay(self):
        # Selecting prices and dates
        prices = self.stock[:, 1].reshape(-1, 1)
        dates = self.stock[:, 0].reshape(-1, 1)

        # Train and fit
        input = 1
        output = 1

        layers = [('F', self.hidden), ('AF', 'tanh'), ('F', self.hidden), ('AF', 'tanh'), ('F', self.hidden), ('AF', 'tanh'), ('F', output)]
        mlpr = ANNR([input], layers, batchSize = 256, maxIter = self.iterations, tol = self.tolerance, reg = 1e-4, verbose = True)
        holdDays = 5
        totalDays = len(dates)
        mlpr.fit(dates[0:(totalDays-holdDays)], prices[0:(totalDays-holdDays)])

        # Predict
        pricePredict = mlpr.predict(dates)

        # Plot the graph
        mpl = Figure
        mpl.plot(dates, prices)
        mpl.plot(dates, pricePredict, c='#5aa9ab')
        return mpl

    