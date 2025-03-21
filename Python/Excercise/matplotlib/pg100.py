import matplotlib.pyplot as plt 
x=["Vijay", "Jay", "Ajay"] 
y=[90,80,70] 
plt.subplot(131) 
plt.bar(x,y) 
plt.subplot (132) 
plt.scatter(x,y) 
plt.subplot(133) 
plt.plot(x,y, "^k") 
plt.show()