#series object pg13
import pandas as pd
x = pd.Series([1,2,3],index = ['a','b','c'])

print("Shape :",x.shape)
print("Size : ",x.size)
print("Index : ",x.index)
print("Dimension : ",x.ndim)
print("Value : ",x.values)
print("Data Type :",x.dtype)
print("Bytes :",x.nbytes)
print("isempty :",x.empty)
print("is empty",x.hasnans)