import pandas as pd

titanicgente = pd.read_csv("titanic_test.csv")

#titanicgente.info()

titanicgente.size()

print(titanicgente["Name"])
