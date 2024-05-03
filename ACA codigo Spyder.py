import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

octubre = pd.read_csv("C:/Users/User1/Desktop/Big Data/EXPO OCTUBRE 2023.csv", sep=",")
octubre['MES']="OCT"
noviembre = pd.read_csv("C:/Users/User1/Desktop/Big Data/EXPO NOVIEMBRE 2023.csv", sep=",")
noviembre['MES']="NOV"
diciembre = pd.read_csv("C:/Users/User1/Desktop/Big Data/EXPO DICIEMBRE 2023.csv", sep=",")
diciembre['MES']="DIC"

var = octubre.dtypes

trimestre = pd.concat([octubre, noviembre, diciembre])

plt.bar(trimestre['MES'],trimestre['FOBDOL'].sum())

octubre['FOBPES'] = octubre['FOBPES'].astype(np.int64)
noviembre['FOBPES'] = noviembre['FOBPES'].astype(np.int64)
diciembre['FOBPES'] = diciembre['FOBPES'].astype(np.int64)
octubre.to_csv("C:/Users/User1/Desktop/Big Data/EXPO OCTUBRE 2023 FINAL.csv", index=False)
noviembre.to_csv("C:/Users/User1/Desktop/Big Data/EXPO NOVIEMBRE 2023 FINAL.csv", index=False)
diciembre.to_csv("C:/Users/User1/Desktop/Big Data/EXPO DICIEMBRE 2023 FINAL.csv", index=False)
trimestre.to_csv("C:/Users/User1/Desktop/Big Data/EXPO TRIMESTRE 2023 FINAL.csv", index=False)
