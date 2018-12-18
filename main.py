import numpy as np
import matplotlib.pyplot as plt
import re

filename = input("What file would you like to open: ")
answer = input("Would you like a line or scatterplot: ")

with open((filename + ".txt"), 'r') as f:
	lines = f.readlines()

x = []
y = []
for line in lines:
	a = re.findall(r"^\d{1,3}", line)
	b = re.findall(r"\d\.\d{1,3}", line)
	x.append(a)
	y.append(b)

for i in range(0, 7):
	x.pop(0)
	y.pop(0)

print(x, "\n", y)

plt.title("Natural Log of Absorbance Over Time")
plt.xlabel('Time')
plt.ylabel('ln(Concentration)')

for i in range(0, len(x)):
	x[i] = float(x[i][0])
for i in range(0, len(y)):
	y[i] = np.log(float(y[i][0]))

print(np.log(25))

#print(y)

m = 0
z = 0

for i in range(0, len(x)):
	m += x[i]
	z += y[i]

d = (y[len(y) - 1] - y[0]) / (x[len(x) - 1] - x[0])

fit = np.polyfit(x, y, 1)
fit_fn = np.poly1d(fit)

plt.plot(x, y, 'yo', x, fit_fn(x), "--k")

print("Line of best fit: ", d, "x", " +", y[0])

if answer == "line":
	plt.plot(x, y)

else:
	plt.scatter(x, y)

plt.show()
