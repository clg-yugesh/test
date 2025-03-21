import pandas as pd 
import numpy as np 

#map()
a = pd.Series (['Java', 'C', 'C++', np.nan]) 
print (a.map({'Java': 'Core', "C": 'Python'})) 
print("____________________________________")


#std()
print("Series:",np.std([1,2,3,4,5])) 
print("____________________________________")


#count(0)
i = pd.Series ([2, 1, 1, np.nan, 3,4,5,5]) 
print(i.count())