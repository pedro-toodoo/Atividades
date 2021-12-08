import numpy as np
import pandas as pd

lista = [10, 20, 30, 40, 50]
dic = {"id1": 1, "id2": 2, "id3": 3}
arr = np.array([1, 2, 3, 4, 5])

print(pd.Series(lista))
print(pd.Series(dic))
print(pd.Series(arr))

#mudar tipo de índice
series1 = pd.Series([1,2,3,4,5], index=["Brasil", "Argentina", "Uruguai", "Chile", "USA"])
print(series1)