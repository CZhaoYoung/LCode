import numpy as np
import pandas as pd
from sklearn.datasets import load_boston


def PolynomialRegression_reg(x,t,M,lam):
    X = np.array([x**m for m in range(M+1)]).T
    w = np.linalg.inv(X.T@X + lam*np.eye(M+1))@X.T@t
    y = X@w
    e = t-y
    return w, y, e


data = load_boston(return_X_y=False)

df = pd.DataFrame(np.hstack((data.data,data.target[:,np.newaxis])),
                  columns=np.hstack((data.feature_names,['House Value'])))

X = df[['LSTAT', 'RM']].to_numpy()
Y = df['House Value'].to_numpy()
M = 10
lam = 0.001

PolynomialRegression_reg(X, Y, M, lam)