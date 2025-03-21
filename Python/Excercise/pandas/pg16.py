
#filer page no 16

import numpy as np 
import pandas as pd 
arr=np.array(([20,30,40], [50,70,80])) 
df=pd.DataFrame (arr,index=["Vijay", "Jay"],columns= 
["Physics", "Chemistry", "Maths"]) 
print (df) 
print(df.filter(items=["Physics"]))