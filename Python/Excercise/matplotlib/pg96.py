import matplotlib.pyplot as plt
plt.title("Line graph")
plt.plot([1,4,5],[5,3,2],'r',linewidth = 5, label = "line1")
plt.plot([1,5,3],[6,4,9],'k',linewidth = 5, lable="line1")
plt.legend()
plt.grid(True)
plt.show()