import numpy as np
import pandas as pd

df = pd.read_excel("Superstore.xls")
print(df)

furniture = df.loc[df['Category'] == 'Furniture']
furniture
furniture['Order Date'].min(), furniture['Order Date'].max()
