#Import the required libraries
import numpy as np
import matplotlib.pyplot as plt
from objects import Charges

#CONSTANTS
K = 9 * np.pow(10, 9)

#Create charges and store as objects
store_Charges = Charges()
stop = False
count = 0

while stop == False:
    count+=1
    
    print(f"Input parameters for point charge {count}:")
    print("Charge: (+ or - value): ", end='')
    charge = float(input())
    print("X-coordinate: ", end='')
    x_cord = float(input())
    print("Y-coordinate: ", end='')
    y_cord = float(input())

    store_Charges.add_Charges(charge, [x_cord, y_cord])

    valid = False
    while valid == False:
        print("Would you like to create another point charge? (Y/N): ", end='')
        choice = input()
        if choice.upper() == "N":
            stop = True
            valid = True
        elif choice.upper() == "Y":
            valid = True
        else:
            print("Please input Y or N.")

#Initialize and calculate vectors
c = 40
max = c/2
x = np.linspace(-max, max, c*2)
y = np.linspace(-max, max, c*2)
X, Y = np.meshgrid(x, y)
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)
for i in range(len(x)):
    for j in range(len(y)):
        for k in range(store_Charges.length):
            x_dist = x[i] - store_Charges.charges[k].coordinates[0]
            y_dist = y[j] - store_Charges.charges[k].coordinates[1]
            r = np.sqrt(x_dist**2 + y_dist**2)

            if x_dist != 0:
                x_dir = K * (store_Charges.charges[k].charge) / (r**2) * (x_dist / r)

            if y_dist != 0:
                y_dir = K * (store_Charges.charges[k].charge) / (r**2) * (y_dist / r)

            Ex[j, i] += x_dir
            Ey[j, i] += y_dir

#Create the plot and plot the vectors as a streamplot
fig, ax = plt.subplots()
ax.set_aspect('equal')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Electric field lines of points charges")
ax.streamplot(X, Y, Ex, Ey, color = "grey", density = 2)
for k in range(store_Charges.length):
    plt.plot(store_Charges.charges[k].coordinates[0], store_Charges.charges[k].coordinates[1], "o", markersize = 10)

plt.show()
