#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def explained_variance():
    df = pd.read_csv("src/data.tsv",sep='\t')
    pca = PCA(10)
    pca.fit(df)
    var = df.var()
    return var.tolist(), pca.explained_variance_

def main():
    v, ev = explained_variance()
    print("The variances are:", " ".join(f"{var:.3f}" for var in v))
    print("The explained variances after PCA are:", " ".join(f"{var:.3f}" for var in ev))
    plt.plot(np.arange(1,len(ev)+1),np.cumsum(ev))
    plt.show()

if __name__ == "__main__":
    main()
