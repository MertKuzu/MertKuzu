import matplotlib.pyplot as plt
import numpy as np

'''
x = [1,2,3,4]
y = [1,4,9,16]

# plt.plot(x,y, color = "red", linewidth = "5")
plt.plot(x,y, "o--r")
plt.axis([0,6,0,20])       #wide graph

plt.title("Graph Title")
plt.xlabel("x label")
plt.ylabel("y label")
'''
'''
x = np.linspace(0,2,100)

plt.plot(x, x, label = "linear")
plt.plot(x, x**2, label = "quadratic")
plt.plot(x, x**3, label = "cubic")
plt.title("Graph Title")
plt.xlabel("x label")
plt.ylabel("y label")

plt.legend()

plt.show()

'''
# axs[0].plot(x, x, color="red")
# axs[0].set_title("lineer")

# axs[1].plot(x, x**2, color="green")
# axs[1].set_title("quadratic")

# axs[2].plot(x, x**3, color="blue")
# axs[2].set_title("cubic")


# x = np.linspace(0,2,100)
# fig,axs = plt.subplots(2,2)

# fig.suptitle("Graph Title")

# axs[0,0].plot(x, x, color="red")
# axs[0,0].set_title("lineer")

# axs[0,1].plot(x, x**2, color="green")
# axs[0,1].set_title("quadratic")

# axs[1,0].plot(x, x**3, color="blue")
# axs[1,0].set_title("cubic")

# axs[1,1].plot(x, x**4, color="yellow")
# axs[1,1].set_title("tetratic")


# plt.tight_layout()

# plt.show()



import pandas as pd

df = pd.read_csv("54.2_nba.csv")
df = df.drop(["Number"], axis = 1).groupby("Team").mean()

df.plot(subplots=True)
plt.legend()

plt.show()