#column selection from a dataframe pg 21
from pandas import DataFrame, Series 
x={'Id': Series ([1,2,3,4,5]), "Name": Series(["A", "B", "C", "D", "E"])} 
df=DataFrame (x) 
print (df) 
print (df ['Id']) 
print (df ["Name"])