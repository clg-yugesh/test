#row addition from dataframe
import pandas as pd
from pandas import DataFrame, Series 
x={'Id': Series ([1,2,3,4,5], index=['a', 'b', 'c', 'd ', 'e']), "Name": Series(["A", "B", "C"],index=['a', 'b','c']) } 
df = DataFrame (x) 
d = DataFrame({"Subject": Series ([1,2,3], index=['a','b','c'])}) 
df=pd.concat([df,d],ignore_index=True)
print(df)