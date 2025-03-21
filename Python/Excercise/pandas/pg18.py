#creating dataframe pg18
#importing the pandas library 
import pandas as pd 
#empty DataFrame 
df = pd. DataFrame() 
print (df) 
# Using List 
list=["Rays", "Tech", "Sunilos"] 
print (pd.DataFrame (list)) 
# using Dict 
info = {'ID' : [101, 102, 103], 'Department' 
: ['B.Sc', 'B.Tech', 'M.Tech',]} 
print (pd.DataFrame (info))